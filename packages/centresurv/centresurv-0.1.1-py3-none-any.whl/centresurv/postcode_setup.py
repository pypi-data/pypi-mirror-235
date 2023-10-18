"""
   Module containing all functions required to perform geospatial analysis and set up a database containing node
   location data, population, area info, nearest network node and shortest path.
"""


from datetime import datetime
import os.path
import sqlite3
import logging as log
import osmnx as ox
import networkx as nx
import pandas as pd
import igraph as ig
import numpy as np

log.basicConfig(filename="SetupLog.log", level=log.DEBUG,
                format="%(asctime)s - %(levelname)s - %(message)s")


def retrieve_graph(area, mode="drive", save=True):
    """
    Retrieve map for area of interest and return the routable network for the chosen mode of transport as a graph.
    This graph can also be saved as a .graphml file if desired.

    Parameters:
    area(str): Name of area to be studied
    mode(str): Mode of transport for graph retrieval; Default = drive
    save(bool): True = Save graph as .graphml file
                False = Do not save graph

    Returns:
    area_graph(MultiDiGraph): Graph representing the drivable road network to be studied
    """
    print("Retrieving Graph", datetime.now())
    start = datetime.now()
    result = 1
    # Retrieve graph using OSMNx
    while True:
        try:
            area_graph = ox.graph_from_place(area, network_type=mode, which_result=result)
            break
        except TypeError:
            result += 1
            area_graph = None
            continue
        except KeyError:
            log.error("%s does not exist or is not defined as a polygon", area)
            raise KeyError("%s could not be found" % area)
    print("Graph retrieved", datetime.now())
    log.info("Map retrieved for %s using Nominatim query result %s", area, result)
    log.debug("Time taken to retrieve graph %s", datetime.now() - start)

    # Save graph locally
    if save is True:
        ox.save_graphml(area_graph, area + ".graphml")
        log.info("graphml file created for %s", area)
        print("Graph saved", datetime.now())
    elif save is False:
        log.info("Graph not saved")
        pass
    else:
        log.error("Parameter \"save\" can only take values True or False")
        raise ValueError("Parameter \"save\" can only take values True or False")
    return area_graph


def load_graph(area):
    """Retrieve graph from saved graphml file

       Parameters:
       area(str): Name of area to be studied

       Returns:
       MultiDiGraph: Graph representing the drivable road network to be studied
    """
    print("Loading graph", datetime.now())
    start = datetime.now()
    area_graph = ox.load_graphml(area + ".graphml")
    log.info("Map loaded for for %s", area)
    log.debug("Time taken to load map %s", datetime.now() - start)
    print("Graph loaded", datetime.now())
    return area_graph


def postcode_to_db(area, in_file, setup_level="standard", columns=None):
    """
    Takes postcode data from csv file and writes to SQLite database. csv file must contain columns named "Longitude",
    "Latitude", "Population" and "Postcode"

    Parameters:
    area(str): Name of area to be studied
    in_file(str): Name of csv file containing postcode data for area of interest, including .csv
    setup_level(str): "standard" = Creates database using pre-defined potentially useful columns (UK-optimised)
                      "light" = Creates database using absolute minimum columns required for the most basic analysis
                      "custom" = Creates database using specified columns (must also include columns dict)
    columns(dict): Dictionary containing column names to be used and SQL datatypes in format {column_name: TYPE}

    Returns:
    None
    """
    print("Creating database", datetime.now())
    start = datetime.now()
    con = sqlite3.connect(area+".sqlite")
    cur = con.cursor()
    # Create database with essential columns
    cur.execute("""CREATE TABLE Postcodes(
                   Postcode    VARCHAR  PRIMARY KEY,
                   Latitude    NUMERIC,
                   Longitude   NUMERIC,
                   Population  NUMERIC)""")
    existing_columns = list(pd.read_csv(in_file, engine="c", nrows=1).columns)
    use_columns = ["Postcode", "Latitude", "Longitude", "Population"]
    # Add additional columns either by standard or custom setup
    if setup_level == "standard":
        useful_columns = {"Ward": "VARCHAR", "County": "VARCHAR", "District": "VARCHAR", "Rural/urban": "VARCHAR",
                          "Region": "VARCHAR", "Index of Multiple Deprivation": "INTEGER", "Postcode area": "VARCHAR",
                          "Postcode district": "VARCHAR", "Built Up Area": "VARCHAR",
                          "Built Up Area Sub-Division": "VARCHAR"}
        for column in existing_columns:
            if column in list(useful_columns.keys()):
                use_columns.append(column)
                column_type = useful_columns.get(column)
                query = "ALTER TABLE Postcodes ADD COLUMN \"%s\" %s" % (column, column_type)
                cur.execute(query)
    elif setup_level == "light":
        pass
    elif setup_level == "custom":
        useful_columns = columns
        for column in existing_columns:
            if column in list(useful_columns.keys()):
                use_columns.append(column)
                column_type = useful_columns.get(column)
                query = "ALTER TABLE Postcodes ADD COLUMN \"%s\" %s" % (column, column_type)
                cur.execute(query)
    else:
        log.error("Invalid argument for setup_level, %s", setup_level)
        raise ValueError("Argument \"setup_level\" must be one of \"custom\", \"standard\", \"light\" as a string")
    # Write postcodes to database
    postcode_csv_chunks = pd.read_csv(in_file, engine="c", usecols=use_columns, chunksize=50)
    for chunk in postcode_csv_chunks:
        chunk.to_sql("Postcodes", con, if_exists="append", index=False)
    con.close()
    log.info("%s SQL table created for postcodes in %s", setup_level, area)
    log.debug("Time taken to create postcode table: %s", datetime.now() - start)


def db_exists(area):
    """
       Checks if database has been created for area, and returns the connection to it if True.

       Parameters:
       area(str): Name of area to be studied

       Returns:
       connection(sqlite3.Connection): Connection to database
    """
    if os.path.isfile(area+".sqlite") is True:
        connection = sqlite3.connect(area+".sqlite")
    else:
        log.error("%s.sqlite could not be found", area)
        raise FileNotFoundError("Database for %s could not be found within the directory" % area)
    return connection


def nearest_node(graph, area):
    """
       Find nearest network node for every postcode within database, using a balltree search

       Parameters:
       graph(MultiDiGraph): Graph for the area to be studied
       area(str): Name of the area to be studied

       Returns:
       None
    """
    print("Finding nearest nodes", datetime.now())
    start = datetime.now()
    con = db_exists(area)
    cur = con.cursor()
    # Add column to database for Node_ID
    try:
        cur.execute("ALTER TABLE Postcodes ADD COLUMN Node_ID INTEGER")
        log.info("Node_ID column added to Postcode table")
    except sqlite3.OperationalError:
        log.info("Postcode table already exists for %s", area)
        pass
    x_coordinates = []
    y_coordinates = []
    # Find Nearest network node based on postcode longitude and latitude
    for lat, lon in cur.execute("SELECT Latitude, Longitude FROM Postcodes").fetchall():
        x_coordinates.append(lat)
        y_coordinates.append(lon)
    nodes = list(ox.get_nearest_nodes(graph, np.array(y_coordinates), np.array(x_coordinates), method="balltree"))
    # Write Node_ID to database
    for r_id in cur.execute("SELECT rowid FROM Postcodes").fetchall():
        node = int(nodes[(int(r_id[0])-1)])
        cur.execute("UPDATE Postcodes Set Node_ID=? WHERE rowid=?", (node, r_id[0]))
    con.commit()
    con.close()
    log.info("Nearest nodes found for postcodes in %s", area)
    log.debug("Time taken to find nodes: %s", datetime.now() - start)
    print("Nearest nodes found for postcodes in %s" % area, datetime.now())


def networkx_to_igraph(graph_nx):
    """
    Generates a graph for use in python-igraph using networkx graph data.

    parameters:
    graph_nx(networkx.MultiDiGraph): node labels for area graph from networkx

    returns:
    graph_ig(igraph.Graph): igraph Graph structure with same data as in original graphml file
    """
    # Populate igraph graph structure with nodes and edges from networkx format
    graph_ig = ig.Graph(directed=True)
    graph_ig.add_vertices(list(graph_nx.nodes()))
    graph_ig.add_edges(list(graph_nx.edges()))
    # Copy necessary attributes to new graph structure
    graph_ig.vs["osmid"] = list(nx.get_node_attributes(graph_nx, "osmid").values())
    graph_ig.es["length"] = list(nx.get_edge_attributes(graph_nx, "length").values())
    return graph_ig


def node_id_to_node_index(nodes, name, graph_nx, postcodes=None):
    """
    Associate each postcode and hospital Node_ID for networkx, with node index used as ID in python-igraph

    Parameters:
    nodes(list): List of all node OSMIDs to be used
    name(str): Name of group of nodes i.e. "Source" or "Hospital"
    graph_nx(networkx.MultiDiGraph): graph for area being studied
    postcodes(list): List of all postcodes to be used (necessary for hospital nodes only)

    Returns:
    node_index_df(pandas.DataFrame): Dataframe with columns for OSMID, corresponing index for igraph, +/- postcode
    """
    if name == "Source" or name == "Hospital":
        pass
    else:
        raise ValueError("name must be either \"Source\" or \"Hospital\"")
    if postcodes is not None:
        node_df = pd.DataFrame({name: nodes, "Postcode": postcodes})
    else:
        node_df = pd.DataFrame({name: nodes})
    node_df = pd.DataFrame.drop_duplicates(node_df)
    node_index_df = pd.DataFrame.from_dict({
        name: list(nx.get_node_attributes(graph_nx, "osmid").values()),
        "Node_Index": list(graph_nx.nodes())})
    node_index_df = pd.merge(node_df, node_index_df, how="inner", on=name)
    return node_index_df


def get_node_id(postcodes, area):
    """
    Retrieve Node_ID for given postcode(s) from within database:

    Parameters:
    postcodes(list): Postcodes (including spaces) for the centres of interest
    area(str): Name of area to be studied

    Returns:
    nodes(dict): Keys = Postcodes, Values = OSMID for corresponding postcode
    """
    con = db_exists(area)
    cur = con.cursor()
    nodes = {}
    if isinstance(postcodes, list) is True:
        for post in postcodes:
            node = cur.execute("""SELECT Node_ID
                                  FROM Postcodes
                                  WHERE Postcode=?""", (post,)).fetchone()
            if node is None:
                print("Postcode %s was not found" % post)
                input("To continue press ENTER; To exit press CTRL-c \n")
                log.warning("Postcode %s was not found", post)
            else:
                nodes[post] = int(node[0])
    else:
        raise TypeError("Postcodes must be given as a list of strings")
    con.close()
    log.info("Node_IDs found for %s in %s", postcodes, area)
    return nodes


def hospitals_to_db(area):
    """
    Creates sqlite table in same database as the area to be studied, using csv file containing all potential centres.

    Parameters:
    area(str): Name of area to be studied

    Returns:
    None
    """
    con = db_exists(area)
    cur = con.cursor()
    query = """CREATE TABLE Hospitals(
               \"Organisation Code\"    VARCHAR     PRIMARY KEY,
               Postcode                 VARCHAR,
               Name                     VARCHAR,
               Parent                   VARCHAR,
               FOREIGN KEY(Postcode) REFERENCES Postcodes(Postcode))
               """
    cur.execute(query)
    log.info("Hospital table created for %s", area)
    hospitals = pd.read_csv("hospitals.csv",
                            usecols=["OrganisationCode", "Postcode", "OrganisationName", "ParentName"],
                            engine="c")
    hospitals = hospitals.rename(columns={"OrganisationCode": "Organisation Code",
                                          "OrganisationName": "Name",
                                          "ParentName": "Parent"})
    hospitals.to_sql("Hospitals", con, if_exists="append", index=False)
    con.close()


def simulation(graph, area, hospital_postcodes, columns=("Distance", "Centre"), copy_from=("Distance", "Centre")):
    """
    If the initial analysis has been performed, this function allows additional simulations can be run for how building
    new centres would affect the accessibility. These simulations are then stored to new columns in the existing
    database.

    parameters:
    graph(networkx.MultiDiGraph): networkx graph of area to be studied
    area(str): Name of area to be studied
    hospital_postcodes(list): List of postcodes for the hospitals to be included in the simulation
    columns(tuple): (name for new distance column, name for new centre column); default ("Distance", "Centre")
    copy_from(tuple): (name of old distance column, name of old centre column); default ("Distance", "Centre")

    returns:
    None
    """
    start = datetime.now()
    graph_nx = nx.relabel.convert_node_labels_to_integers(graph)
    graph_ig = networkx_to_igraph(graph_nx)
    node_gdf = ox.graph_to_gdfs(graph, edges=False)

    hospital_dict = get_node_id(hospital_postcodes, area)
    hospital_id = list(hospital_dict.values())
    hospital_pc = list(hospital_dict.keys())

    con = db_exists(area)
    cur = con.cursor()
    # Create new columns for simulation distance and centre
    try:
        cur.execute("ALTER TABLE Postcodes ADD COLUMN \""+columns[0]+"\" INTEGER")
        cur.execute("UPDATE Postcodes SET \""+columns[0]+"\"=\""+copy_from[0]+"\"")
    except sqlite3.OperationalError:
        pass
    try:
        cur.execute("ALTER TABLE Postcodes ADD COLUMN \""+columns[1]+"\" VARCHAR")
        cur.execute("UPDATE Postcodes SET \""+columns[1]+"\"=\""+copy_from[1]+"\"")
    except sqlite3.OperationalError:
        pass
    # Copy data from previous analysis
    cur.execute("UPDATE Postcodes SET \"" + columns[0] + "\"=\"" + copy_from[0] + "\"")
    cur.execute("UPDATE Postcodes SET \"" + columns[1] + "\"=\"" + copy_from[1] + "\"")
    n = 1
    # Find shortest path to each centre where a possible shorter path exists
    for h in hospital_id:
        print("Simulation for centre %s" % n, datetime.now())
        h_id = [hospital_id[n - 1]]
        h_pc = [hospital_pc[n - 1]]
        query = """SELECT Node_ID, Latitude, Longitude, \"%s\"
                   FROM Postcodes
                   WHERE Distance IS NOT NULL""" % columns[0]
        postcode_node_df = pd.read_sql_query(query, con)
        postcode_node_df.drop_duplicates("Node_ID", inplace=True)

        # Use Haversine's equation to determine whether it is possible for a shorter path to exist
        lat1 = np.array(postcode_node_df["Latitude"].to_list())
        lon1 = np.array(postcode_node_df["Longitude"].to_list())
        x = [[float(node_gdf.loc[[h]]["x"])]]
        y = [[float(node_gdf.loc[[h]]["y"])]]
        lon2 = np.array(x)
        lat2 = np.array(y)

        lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        h = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
        c = 2 * np.arcsin(np.sqrt(h))
        d = 6367 * c * 1000
        d = d[0]

        postcode_node_df["Haversine"] = d
        postcode_node_df.rename(columns={"Node_ID": "Source", columns[0]: "Old Distance"}, inplace=True)
        postcode_node_df.drop(postcode_node_df[postcode_node_df["Haversine"] > postcode_node_df["Old Distance"]].index,
                              inplace=True)
        postcode_node_index_df = pd.DataFrame.from_dict({
            "Source": list(nx.get_node_attributes(graph_nx, "osmid").values()),
            "Node_Index": list(graph_nx.nodes())})
        postcode_node_index_df = pd.merge(postcode_node_df, postcode_node_index_df,
                                          how="inner", on="Source")

        hospital_node_index_df = node_id_to_node_index(h_id, "Hospital", graph_nx, h_pc)
        unique_paths = postcode_node_df.count()[0]
        print("Finding shortest paths for %s unique nodes" % unique_paths)

        # Create lists for target and source nodes
        target = list(hospital_node_index_df["Node_Index"])
        source_index = list(postcode_node_index_df["Node_Index"])
        paths = graph_ig.shortest_paths(source_index, target, weights="length")
        # Returns list of lists for shortest path from each source node to each target node
        shortest = []
        centre_osmid = []
        for path in paths:
            # Find overall shortest path
            hospitals = hospital_node_index_df["Postcode"].tolist()
            path_dict = dict(zip(hospitals, path))
            centre_osmid.append(min(path_dict, key=path_dict.get))
            try:
                shortest.append(int(min(t for t in path)))
            except OverflowError:
                shortest.append(0)
                continue
        postcode_node_index_df["New_Distance"] = pd.Series(shortest)
        postcode_node_index_df["New_Centre"] = pd.Series(centre_osmid)

        # Write shortest path to database if shorter than existing shortest path
        postcode_node_index_df = postcode_node_index_df.rename(columns={"Source": "Node_ID"})
        postcode_node_index_df = postcode_node_index_df[postcode_node_index_df["New_Distance"] < postcode_node_index_df["Old Distance"]]
        q1 = "SELECT Node_ID, \"%s\", \"%s\" FROM Postcodes" % (columns[0], columns[1])
        df1 = pd.read_sql_query(q1, con)
        new_df = df1.merge(postcode_node_index_df, how="left", on="Node_ID")
        new_df["New_Distance"] = new_df["New_Distance"].fillna(new_df[columns[0]])
        new_df["New_Centre"] = new_df["New_Centre"].fillna(new_df[columns[1]])
        distances = list(new_df["New_Distance"].values)
        centres = list(new_df["New_Centre"].values)
        for r_id in cur.execute("SELECT rowid FROM Postcodes").fetchall():
            d = distances[(int(r_id[0]) - 1)]
            c = centres[(int(r_id[0]) - 1)]
            cur.execute("UPDATE Postcodes SET \""+columns[0]+"\"=?, \""+columns[1]+"\"=? WHERE rowid=?", (d, c, r_id[0]))
        print("Simulation for centre %s complete %s" % (hospital_postcodes[n-1], datetime.now()))
        print("%s shortest paths found" % unique_paths)
        n += 1
        con.commit()
        log.info("Shortest paths to %s calculated for postcodes in %s", hospital_postcodes[n-2], area)
        log.debug("Time taken to calculate %s paths: %s", unique_paths, datetime.now() - start)
    con.close()
    print("Simulation completed ", datetime.now())


def shortest_paths2(graph, area, hospital_postcodes, distance="Distance", centre="Centre"):
    """
    Find shortest paths for all residential postcodes within database using Dijkstra's algorithm. This does not employ a
    heuristic to find the shortest path to the closest centre first. Hence this function is generally faster when
    studying smaller areas where centres and postcodes are close together.

    Parameters:
    graph(MultiDiGraph): Graph for area to be studied
    area(str): Name of area to be studied
    hospital_dict(dict): Keys = postcodes, Values = OSMID for corresponding postcode
    distance(str): Name of distance column; default is "Distance"
    centre(str): Name of centre column; default is "Centre"

    Returns:
    None
    """
    print("Finding shortest paths ", datetime.now())
    start = datetime.now()
    hospital_dict = get_node_id(hospital_postcodes, area)
    hospitals = list(hospital_dict.values())
    hospital_pc = list(hospital_dict.keys())
    con = db_exists(area)
    cur = con.cursor()
    # Add new columns to database for distance and centre
    try:
        d_query = "ALTER TABLE Postcodes ADD COLUMN %s INTEGER" % distance
        cur.execute(d_query)
    except sqlite3.OperationalError:
        input("Column %s already exists. Press ENTER to continue, or Ctrl-c to exit \n" % distance)
        pass
    try:
        c_query = "ALTER TABLE Postcodes ADD COLUMN %s VARCHAR" % centre
        cur.execute(c_query)
    except sqlite3.OperationalError:
        input("Column %s already exists. Press ENTER to continue, or Ctrl-c to exit \n" % centre)
        pass
    # Create igraph graph from networkx graph data (source: xxx)
    graph_nx = nx.relabel.convert_node_labels_to_integers(graph)
    graph_ig = networkx_to_igraph(graph_nx)

    source = []
    for node_id in cur.execute("""SELECT Node_ID
                                  FROM Postcodes
                                  WHERE Population IS NOT NULL""").fetchall():
        source.append(node_id[0])
    postcode_node_index_df = node_id_to_node_index(source, "Source", graph_nx)
    hospital_node_index_df = node_id_to_node_index(hospitals, "Hospital", graph_nx, hospital_pc)

    # Create lists for target and source nodes
    target = list(hospital_node_index_df["Node_Index"])
    source_index = list(postcode_node_index_df["Node_Index"])
    paths = graph_ig.shortest_paths(source_index, target[0], weights="length")
    # Returns list of lists for shortest path from each source node to the first centre in list
    shortest = []
    centre_osmid = []
    for path in paths:
        # Find overall shortest path
        hospitals = hospital_node_index_df["Postcode"].tolist()
        path_dict = dict(zip(hospitals, path))
        centre_osmid.append(min(path_dict, key=path_dict.get))
        try:
            shortest.append(int(min(t for t in path)))
        except OverflowError:
            shortest.append(0)
            continue
    postcode_node_index_df[distance] = pd.Series(shortest)
    postcode_node_index_df[centre] = pd.Series(centre_osmid)
    print("Writing to database", datetime.now())
    postcode_node_index_df = postcode_node_index_df.rename(columns={"Source": "Node_ID"})
    new_df = pd.read_sql_query("SELECT Node_ID FROM Postcodes", con)
    new_df = new_df.merge(postcode_node_index_df, how="left", on="Node_ID")
    distances = list(new_df[distance].values)
    centres = list(new_df[centre].values)
    for r_id in cur.execute("SELECT rowid FROM Postcodes").fetchall():
        d = distances[(int(r_id[0]) - 1)]
        c = centres[(int(r_id[0]) - 1)]
        q_exe = "UPDATE Postcodes SET %s=?, %s=? WHERE rowid=?" % (distance, centre)
        cur.execute(q_exe, (d, c, r_id[0]))
    print("Centre 1")
    n = 2
    del hospital_pc[0]
    con.commit()
    con.close()
    # repeat shortest path analysis using simulation function for remaining centres
    for t in hospital_pc:
        simulation(graph, area, [t], columns=(distance, centre), copy_from=(distance, centre))
        print("Shortest paths to centre ", n, " found")
        n = n + 1
    log.info("Shortest routes calculated for postcodes in %s", area)
    log.debug("Time taken to calculate paths: %s", datetime.now() - start)
    print("Shortest paths found")
    print(datetime.now() - start)


def shortest_paths(graph, area, hospital_postcodes, distance="Distance", centre="Centre"):
    """
    Find shortest paths for all residential postcodes within database using Dijkstra's algorithm. This uses a heuristic,
    first finding the shortest path to the closest centre by direct distance. This is much faster when looking at large
    geographical areas with spaced out centres. To Re-run analysis with same postcodes but different centres, the
    distance and centre parameters can be changed, to store the results in the same database alongside the initial
    results.

    Parameters:
    graph(MultiDiGraph): Graph for area to be studied
    area(str): Name of area to be studied
    hospital_dict(dict): Keys = postcodes, Values = OSMID for corresponding postcode
    distance(str): Name for distance column; default is "Distance"
    centre(str): Name for distance column; default is "Centre"

    Returns:
    None
    """
    print("Finding shortest paths")
    start = datetime.now()
    hospital_dict = get_node_id(hospital_postcodes, area)
    hospital_id = list(hospital_dict.values())
    hospital_pc = list(hospital_dict.keys())
    node_gdf = ox.graph_to_gdfs(graph, edges=False)
    con = db_exists(area)
    cur = con.cursor()
    # Add new columns to database for distance and centre
    try:
        d_query = "ALTER TABLE Postcodes ADD COLUMN %s INTEGER" % distance
        cur.execute(d_query)
    except sqlite3.OperationalError:
        input("Column %s already exists. Press ENTER to continue, or Ctrl-c to exit \n" % distance)
        pass
    try:
        c_query = "ALTER TABLE Postcodes ADD COLUMN %s VARCHAR" % centre
        cur.execute(c_query)
    except sqlite3.OperationalError:
        input("Column %s already exists. Press ENTER to continue, or Ctrl-c to exit \n" % centre)
        pass
    # Create igraph graph from networkx graph data (source: xxx)
    graph_nx = nx.relabel.convert_node_labels_to_integers(graph)
    graph_ig = networkx_to_igraph(graph_nx)

    # Calculate total number of residential postcodes
    pc_query = """SELECT Population FROM Postcodes WHERE Population IS NOT NULL"""
    pc_df = pd.read_sql_query(pc_query, con)
    print("Finding shortest paths for %s Postcodes" % pc_df.count()[0])

    # Retrieve longitude and latitude for all unique nodes
    query = """SELECT Node_ID, Latitude, Longitude
                       FROM Postcodes"""
    postcode_node_df = pd.read_sql_query(query, con)
    postcode_node_df.drop_duplicates("Node_ID", inplace=True)
    unique_paths = postcode_node_df.count()[0]
    print("%s Unique nodes found" % unique_paths)

    # Find shortest direct distance between all nodes and centres using Haversine's equation
    lat1 = np.array([[lat] for lat in postcode_node_df["Latitude"].to_list()])
    lon1 = np.array([[lon] for lon in postcode_node_df["Longitude"].to_list()])
    x, y = [], []
    for h in hospital_id:
        x.append(node_gdf.at[h, "x"])
        y.append(node_gdf.at[h, "y"])
    lon2 = np.array(x)
    lat2 = np.array(y)

    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    h = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2
    c = 2 * np.arcsin(np.sqrt(h))
    d = 6367 * c * 1000
    shortest = []
    centre_pc = []

    # Find overall closest centre to each node
    for dist in d:
        path_dict = dict(zip(hospital_pc, dist))
        centre_pc.append(min(path_dict, key=path_dict.get))
        try:
            shortest.append(int(min(t for t in dist)))
        except OverflowError:
            shortest.append(0)
            continue
    postcode_node_df["Direct"] = shortest
    postcode_node_df["Direct_Centre"] = centre_pc
    postcode_node_df.rename(columns={"Node_ID": "Source"}, inplace=True)
    postcode_node_index_df = pd.DataFrame.from_dict({
        "Source": list(nx.get_node_attributes(graph_nx, "osmid").values()),
        "Node_Index": list(graph_nx.nodes())})
    postcode_node_index_df = pd.merge(postcode_node_df, postcode_node_index_df,
                                      how="inner", on="Source")
    hospital_node_index_df = node_id_to_node_index(hospital_id, "Hospital", graph_nx, hospital_pc)

    n = 0
    # Find shortest drivable path for each postcode to corresponding nearest centre by direct distance
    for hpc in hospital_pc:
        source_df = postcode_node_index_df[postcode_node_index_df.Direct_Centre == hpc]
        target = [hospital_node_index_df.loc[n, "Node_Index"]]
        source_index = list(source_df["Node_Index"])
        paths = graph_ig.shortest_paths(source_index, target, weights="length")
        shortest = []
        centre_osmid = []
        for path in paths:
            # Find overall shortest path
            hospitals = hospital_node_index_df["Postcode"].tolist()
            path_dict = dict(zip(hospitals, path))
            centre_osmid.append(min(path_dict, key=path_dict.get))
            try:
                shortest.append(int(min(t for t in path)))
            except OverflowError:
                shortest.append(0)
                continue

        source_df["New_Distance"] = shortest
        source_df["New_Centre"] = hpc

        source_df = source_df.rename(columns={"Source": "Node_ID"})
        # source_df = source_df[source_df["New_Distance"] < source_df["Old Distance"]]
        q1 = "SELECT Node_ID FROM Postcodes"
        df1 = pd.read_sql_query(q1, con)
        df1 = df1.merge(source_df, how="left", on="Node_ID")
        if n == 0:
            new_df = df1
            pass
        else:
            new_df["New_Distance"] = new_df["New_Distance"].fillna(df1["New_Distance"])
            new_df["New_Centre"] = new_df["New_Centre"].fillna(df1["New_Centre"])
            continue
        n += 1
    distances = list(new_df["New_Distance"].values)
    centres = list(new_df["New_Centre"].values)

    # Write shortest distances to database
    for r_id in cur.execute("SELECT rowid FROM Postcodes").fetchall():
        d = distances[(int(r_id[0]) - 1)]
        c = centres[(int(r_id[0]) - 1)]
        q_exe = "UPDATE Postcodes SET %s=?, %s=? WHERE rowid=?" % (distance, centre)
        cur.execute(q_exe, (d, c, r_id[0]))
    con.commit()
    con.close()
    print("Initial matching complete ", datetime.now())
    print("%s shortest paths found" % unique_paths)
    log.info("Initial matching for %s complete", area)
    log.debug("Time taken to calculate %s paths: %s", unique_paths, datetime.now() - start)
    # Use simulaton function to iterate over list of centres and determine shortest paths to each where necessary
    simulation(graph, area, hospital_postcodes, columns=(distance, centre), copy_from=(distance, centre))
    print(datetime.now() - start)


def complete_setup(area, postcode_csv, hospital_postcodes, distance="Distance", centre="Centre", setup="standard",
                   columns=None):
    """
    Single function to be called, if wishing to setup database with postcode data and perform shortest path analysis.
    N.B. This uses the shortest_paths2 function to find the shortest paths and so may be slower if studying smaller
    areas with closely packed centres.

    parameters:
    area(str): Name of area to be studied
    postcode_csv(str): Name of csv file containing postcode data for area of interest, including .csv
    hospital_postcodes(list): List of postcodes of centres to be used in shortest path analysis
    distance(str): Name of distance column; default is "Distance"
    centre(str): Name of centre column; default is "Centre"
    setup(str): Level of setup. refer to postcode_to_db for kwargs
    columns(dict): {column_name: TYPE}, refer to postcode_to_db for explanation

    returns:
    None
    """
    postcode_to_db(area, postcode_csv, setup, columns)
    try:
        graph = load_graph(area)
    except FileNotFoundError:
        graph = retrieve_graph(area, save=True)
    nearest_node(graph, area)
    shortest_paths(graph, area, hospital_postcodes, distance, centre)
    print("Setup complete")
