"""
    This module contains a series of functions to calculate various statistics and  sub-area analysis,
    along with basic visualisation using matplotlib
"""

import logging as log
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sqlite3
from datetime import datetime
import geoserv.postcode_setup as ps
from scipy import stats

log.basicConfig(filename="SetupLog.log", level=log.DEBUG,
                format="%(asctime)s - %(levelname)s - %(message)s")


def validate_subarea(area, subarea):
    """
    Checks if the subarea chosen for analysis exists as a column within the database table.

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea for comparative analysis

    Returns:
    column(bool): True if subarea exists, false if not
    """
    con = ps.db_exists(area)
    pragma = pd.read_sql_query("Pragma table_info(Postcodes)", con)
    columns = list(name[2] for name in pragma.itertuples())
    if subarea not in columns:
        print("%s is not a column within the database, must be one of %s" % (subarea, columns))
        log.error("%s is not a column within the database for %s", subarea, area)
        con.close()
        column = False
    else:
        con.close()
        column = True
    return column


def sub_area(area, subarea):
    """
    Returns list of unique subarea names in chosen subarea category

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea category for analysis

    Returns:
    sub_list(list): List of subareas in chosen subarea category
    """
    con = ps.db_exists(area)
    if validate_subarea(area, subarea) is True:
        query = "SELECT \"%s\" FROM Postcodes WHERE Population IS NOT NULL" % subarea
        subarea_df = pd.read_sql_query(query, con)
        subarea_df = subarea_df.drop_duplicates().values.tolist()
        sub_list = list(a[0] for a in subarea_df)
    else:
        raise ValueError("Subarea %s does not exist within the database for %s" % (subarea, area))
    con.close()
    return sub_list


def pop_dist_retrieve(area, subarea, distance="Distance"):
    """
    Retrieve and return population and distances for subareas, for further analysis

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea category for analysis
    distance(str): Distance measure to be used in analysis; default="Distance

    Returns:
    results(dict): keys=name of subarea, value = data frame containing population and distance
    """
    con = ps.db_exists(area)
    sub_list = sub_area(area, subarea)
    results = {}
    for sub in sub_list:
        query = """SELECT Population, \"%s\"
                   FROM Postcodes
                   WHERE \"%s\" = \"%s\"
                   AND Population IS NOT NULL""" % (distance, subarea, sub)
        postcode_distance_df = pd.read_sql_query(query, con)
        results[sub] = postcode_distance_df
    con.close()
    return results


def correlation(area, var1, var2):
    """
        Calculate the correlation coefficient between two columns within the database.

        Parameters:
        area(str): Name of area to be studied
        var1(str): Column name for variable 1
        var2(str): Column name for variable 2

        Returns:
        corr(float): Correlation coefficient between the two variables
        """
    con = ps.db_exists(area)
    query = "SELECT \"%s\", \"%s\" FROM Postcodes WHERE Population IS NOT NULL" % (var1, var2)
    comparison_df = pd.read_sql_query(query, con)
    v1 = np.array(comparison_df[var1])
    v2 = np.array(comparison_df[var2])
    con.close()
    corr = np.corrcoef(v1, v2)
    return corr[0, 1]


def bar_chart(subarea, metric, measures, results_df_list, population=False):
    """
    Create bar chart displaying 1 or 2 sets of data side-by-side

    parameters:
    subarea(str): Name of subarea category for analysis
    metric(str): Name of metric for y-axis label
    measures(list): List of distance measures
    results_df_list(list): List of DataFrames containing data, must contain subarea column and data columns
    population(bool): If true, uses population for subarea as comparator

    returns:
    plt(): bar chart
    """
    if len(measures) == 2:
        merged_df = results_df_list[0].merge(results_df_list[1], how="inner", on=subarea)
    else:
        merged_df = results_df_list[0]
    width = 0.35
    m = -1
    names = merged_df[subarea].values.tolist()
    if population is True:
        measures.append("Population")
    else:
        pass
    fig, ax1 = plt.subplots()
    ax = 1
    for measure in measures:
        data = merged_df[measure].values.tolist()
        if ax == 1:
            axis = ax1
            ax1.set_xticks(np.array(range(len(names))))
            ax1.set_xticklabels(names, rotation="vertical")
            colour = "tab:blue"
        elif ax == 2:
            axis = ax1.twinx()
            colour = "tab:orange"
        else:
            raise(ValueError("Only the original distance and one comparison/population can be included"))
        axis.set_ylabel(measure)
        axis.bar(np.array(range(len(data))) + (m * width) / 2, data, width=width, align="center", color=colour, label=measure)
        m = -m
        axis.tick_params(axis="y")
        axis.legend()
        ax += 1
    log.info("Bar graph created for %s by sub-area %s", metric, subarea)
    log.debug("Bar chart created for %s", measures)
    return plt


def scatter_plot(subarea, metric, measures, results_df_list, population=False):
    if len(measures) == 2:
        merged_df = results_df_list[0].merge(results_df_list[1], how="inner", on=subarea)
    else:
        merged_df = results_df_list[0]
    width = 0.35
    m = -1
    names = merged_df[subarea].values.tolist()
    if population is True:
        measures.append("Population")
    else:
        pass
    fig, ax1 = plt.subplots()
    data = merged_df[measures[0]].values.tolist()
    population = merged_df[measures[1]].values.tolist()
    ax1.scatter(population, data)
    ax1.set_ylabel(measures[0])
    ax1.set_xlabel(measures[1])
    ax1.plot()
    corr1 = stats.pearsonr(merged_df[measures[0]].values.tolist(), merged_df[measures[1]].values.tolist())
    log.info("Scatter graph created for %s by sub-area %s", metric, subarea)
    log.debug("Scatter chart created for %s", measures)
    print("r=%s, p=%s" % (corr1[0], corr1[1]))
    return plt


def person_meters(area, subarea=None, ordered=True, graph=False, distance="Distance", comparison=None, ex_comp=None,
                  ex_comp_name="Comparison"):
    """
    Calculates person meters either as a total (default) or by subarea of choice

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Default=None; Name of subarea category for analysis
    ordered(bool): Default=True; Orders values within the results based on value
                   N.B. This only has effect when the subarea parameter is not None
    graph(bool): Default=False; Option to visulise data as bar chart for subarea breakdown using matplotlib
                 N.B. This will only have an effect if subarea parameter is not None
    distance(str): Distance column to be used
    comparison(str): Optional distance column to be used
    ex_comp(dict): keys=index, values=[subarea name, value]; use to compare distance data against
    ex_comp_name(str): Label to appear on axis of graph when using external comparison

    Returns:
    results(dict): Dictionary containing breakdown of person-meters by subarea
    """
    con = ps.db_exists(area)
    results_df_list = []
    results_list = []
    if comparison == "Population":
        measures = [distance]
    elif comparison is not None:
        measures = [distance, comparison]
    else:
        measures = [distance]
    for measure in measures:
        pm_dict = {}
        if subarea is not None:
            results = pop_dist_retrieve(area, subarea, measure)
            for sub, postcode_distance_df in results.items():
                pm_sum = 0
                for row in postcode_distance_df.itertuples():
                    try:
                        pm_sum += int(row[1]*row[2])
                    except ValueError:
                        continue
                pm_dict[sub] = pm_sum
                log.info("Total person meters for %s = %s", sub, pm_sum)
            results_df = pd.DataFrame({subarea: list(pm_dict.keys()), measure: list(pm_dict.values())})
            if ordered is True:
                results_df = results_df.sort_values(measure)
            else:
                pass
            results_df_list.append(results_df)
        else:
            query = "SELECT Population, \"%s\" FROM Postcodes WHERE Population IS NOT NULL" % measure
            postcode_distance_df = pd.read_sql_query(query, con)
            pm_sum = 0
            for row in postcode_distance_df.itertuples():
                try:
                    pm_sum += int(row[1]*row[2])
                except ValueError:
                    continue
            pm_dict[measure] = pm_sum
            log.info("Total person meters for %s = %s", area, pm_sum)
        results_list.append(pm_dict)
    con.close()
    if ex_comp is not None:
        measures.append(ex_comp_name)
        results_list.append(ex_comp)
        ex_comp_df = pd.DataFrame.from_dict(ex_comp, orient="index", columns=[subarea, ex_comp_name])
        results_df_list.append(ex_comp_df)
    else:
        pass
    if graph is True:
        if comparison == "Population":
            bar_chart(subarea, "Median Distance", measures, results_df_list, True).show()
        else:
            bar_chart(subarea, "Median Distance", measures, results_df_list, False).show()
    else:
        pass
    return results_list


def mean_distance(area, subarea=None, ordered=True, graph=False, distance="Distance", comparison=None, ex_comp=None,
                  ex_comp_name="Comparison"):
    """
    Calculates the mean distance of travel either in total or per subarea.

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea category for analysis
    ordered(bool): Default=True; Orders values within the results based on value
                   N.B. This only has effect when the subarea parameter is not None
    graph(bool): Default=False; Option to visualise data as bar chart for subarea breakdown using matplotlib
                 N.B. Naturally this will only be possible if subarea parameter is not None
    distance(str): Distance column to be used
    comparison(str): Optional distance column to be used
    ex_comp(dict): keys=index, values=[subarea name, value]; use to compare distance data against
    ex_comp_name(str): Label to appear on axis of graph when using external comparison

    Returns:
    results(dict): Returns dictionary with mean travel distance per subarea studied
    """
    con = ps.db_exists(area)
    results_df_list = []
    results_list = []
    if comparison == "Population":
        measures = [distance]
    elif comparison is not None:
        measures = [distance, comparison]
    else:
        measures = [distance]
    for measure in measures:
        mean_dict = {}
        if subarea is not None:
            results = pop_dist_retrieve(area, subarea, measure)
            for sub, postcode_distance_df in results.items():
                pm_sum = 0
                pop = 0
                for row in postcode_distance_df.itertuples():
                    try:
                        pm_sum += int(row[1] * row[2])
                        pop += int(row[1])
                    except ValueError:
                        continue
                try:
                    mean = int(pm_sum/pop)
                except ZeroDivisionError:
                    mean = 0
                mean_dict[sub] = mean
                log.info("Mean travel distance in %s = %s", sub, pop)
            results_df = pd.DataFrame({subarea: list(mean_dict.keys()), measure: list(mean_dict.values())})
            if ordered is True:
                results_df = results_df.sort_values(measure)
            else:
                pass
            results_df_list.append(results_df)
        else:
            query = "SELECT Population, \"%s\" FROM Postcodes WHERE Population IS NOT NULL" % measure
            population_distance_df = pd.read_sql_query(query, con)
            total_pm = 0
            pop = 0
            for row in population_distance_df.itertuples():
                try:
                    total_pm += int(row[1] * row[2])
                    pop += int(row[1])
                except TypeError:
                    continue
            mean = int(total_pm/pop)
            mean_dict[measure] = mean
            log.info("Mean distance for %s = %s", area, mean)
        results_list.append(mean_dict)
    con.close()
    if ex_comp is not None:
        measures.append(ex_comp_name)
        results_list.append(ex_comp)
        ex_comp_df = pd.DataFrame.from_dict(ex_comp, orient="index", columns=[subarea, ex_comp_name])
        results_df_list.append(ex_comp_df)
    else:
        pass
    if graph is True:
        if comparison == "Population":
            bar_chart(subarea, "Median Distance", measures, results_df_list, True).show()
        else:
            bar_chart(subarea, "Median Distance", measures, results_df_list, False).show()
    else:
        pass
    return results_list


def median_distance(area, subarea=None, ordered=True, graph=False, distance="Distance", comparison=None, ex_comp=None,
                    ex_comp_name="Comparison"):
    """
    Calculates median distance of travel either in total or per subarea.

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea category for analysis
    ordered(bool): Default=True; Orders values within the results based on value
                   N.B. This only has effect when the subarea parameter is not None
    graph(bool): Default=False; Option to visualise data as bar chart for subarea breakdown using matplotlib
                 N.B. Naturally this will only be possible if subarea parameter is not None
    distance(str): Distance column to be used
    comparison(str): Optional distance column to be used
    ex_comp(dict): keys=index, values=[subarea name, value]; use to compare distance data against
    ex_comp_name(str): Label to appear on axis of graph when using external comparison

    Returns:
    results(dict): Dictionary containing median travel distance by subarea
    """
    con = ps.db_exists(area)
    results_df_list = []
    results_list = []
    if comparison == "Population":
        measures = [distance]
    elif comparison is not None:
        measures = [distance, comparison]
    else:
        measures = [distance]
    for measure in measures:
        med_dict = {}
        pop_dict = {}
        if subarea is not None:
            results = pop_dist_retrieve(area, subarea, measure)
            for sub, postcode_distance_df in results.items():
                distances = []
                total_pop = 0
                for row in postcode_distance_df.itertuples():
                    try:
                        dist = int(row[2])
                        if dist is None:
                            dist = 10
                        pop = int(row[1])
                        total_pop += pop
                        dist_list = [dist] * pop
                        for distance in dist_list:
                            distances.append(int(distance))
                    except ValueError:
                        continue
                distances = np.array(distances, dtype=np.int64)
                try:
                    median = int(np.median(distances))
                except ValueError:
                    median = 0
                med_dict[sub] = median
                pop_dict[sub] = total_pop
                log.info("Median distance for %s = %s", sub, median)
            results_df = pd.DataFrame({subarea: list(med_dict.keys()),
                                       measure: list(med_dict.values()),
                                       "Population": list(pop_dict.values())})
            if ordered is True:
                results_df = results_df.sort_values(measure)
            else:
                pass
            results_df_list.append(results_df)
        else:
            query = "SELECT Population, \"%s\" FROM Postcodes WHERE Distance IS NOT NULL" % measure
            population_distance_df = pd.read_sql_query(query, con)
            distances = []
            for row in population_distance_df.itertuples():
                try:
                    dist = row[2]
                    if dist is None:
                        dist = 10
                    pop = int(row[1])
                    dist_list = [dist] * pop
                    for distance in dist_list:
                        distances.append(int(distance))
                except ValueError:
                    continue
            distances = np.array(distances, dtype=np.int64)
            median = int(np.median(distances))
            med_dict[measure] = median
            print(np.amin(distances))
            print(np.percentile(distances, [25, 75]))
            print(np.amax(distances))
            log.info("Median distance for %s = %s", area, median)
        results_list.append(med_dict)
    con.close()
    if ex_comp is not None:
        measures.append(ex_comp_name)
        results_list.append(ex_comp)
        ex_comp_df = pd.DataFrame.from_dict(ex_comp, orient="index", columns=[subarea, ex_comp_name])
        results_df_list.append(ex_comp_df)
    else:
        pass
    if graph is True:
        if comparison == "Population":
            scatter_plot(subarea, "Median Distance", measures, results_df_list, True).show()
        else:
            bar_chart(subarea, "Median Distance", measures, results_df_list, False).show()
    else:
        pass
    return results_list


def lorenz(area, measures, step=1):
    """
    Plot Lorenz curve using distance data for individuals in matplotlib.

    Parameters:
    area(str): Name of area to be studied
    measures(list):
    step(int): Every nth value to be selected for generating graph; larger step = more crude approximation

    Returns:
    plt(): matplotlib graph with lorenz curve
    half_distances(dict) = {measure: value} value is proportion of population accounting fo 50% of travel distance
    """
    start = datetime.now()
    con = ps.db_exists(area)
    half_distances = {}
    for measure in measures:
        query = """SELECT Population, \"%s\"
                   FROM Postcodes
                   WHERE Population IS NOT NULL""" % measure
        population_distance_df = pd.read_sql_query(query, con)
        population_distance_df.sort_values(by=[measure], inplace=True)
        distances = []
        for row in population_distance_df.itertuples():
            distance = row[2]
            if distance is None:
                distance = 10
            population = int(row[1])
            distance_enum = [distance] * population
            for value in distance_enum:
                distances.append(int(value))
        distances = np.array(distances, dtype=np.int64)
        distances = np.sort(distances)
        distances += 1
        distances = distances[::step]
        x_lorenz = distances.cumsum() / distances.sum()
        x_lorenz = np.insert(x_lorenz, 0, 0)
        plt.plot(np.arange(x_lorenz.size)/(x_lorenz.size-1), x_lorenz, label=measure)
        log.info("Lorenz curve generated for %s", area)
        log.debug("Time to generate lorenz curve: %s", datetime.now() - start)
        half_distance = 1 - min(range(len(x_lorenz)), key=lambda x: abs(x_lorenz[x]-0.5))/len(x_lorenz)
        half_distances[measure] = half_distance
        print("In %s, %s account for half of total travel distance" % (measure, half_distance))
    plt.legend()
    plt.xlabel("Cumulative Population")
    plt.ylabel("Cumulative Distance")
    plt.plot([0, 1], [0, 1], color="k")
    con.close()
    return plt, half_distances


def gini(area, graph=False, sim_distance="Distance", comparison=None):
    """
    Calculates Gini coefficient for distribution of travel distance within the population. Results will be in range 0-1
    where 0 is perfect equality and 1 is perfect inequality.

    Parameters:
    area(str): Name of area to be studied
    graph(bool): Generate Lorenz curve from same data
    sim_distance(str): Distance column to be used
    comparison(str): Optional additional distance column to be used

    Returns:
    gini_dict(dict): {measure: gini coefficient}
    """
    con = ps.db_exists(area)
    if comparison is not None:
        measures = [sim_distance, comparison]
    else:
        measures = [sim_distance]
    gini_dict = {}
    for measure in measures:
        query = """SELECT Population, \"%s\"
                   FROM Postcodes
                   WHERE Population IS NOT NULL""" % measure
        population_distance_df = pd.read_sql_query(query, con)
        distances = []
        for row in population_distance_df.itertuples():
            distance = row[2]
            if distance is None:
                distance = 10
            population = int(row[1])
            distance_enum = [distance] * population
            for value in distance_enum:
                distances.append(int(value))
        distances = np.array(distances, dtype=np.int64)
        distances = np.sort(distances)
        distances += 1
        index = np.arange(1, distances.shape[0]+1)
        number = distances.shape[0]
        gini_coefficient = (float(np.sum((2 * index - number - 1) * distances)) / (number * np.sum(distances)))
        gini_dict[measure] = gini_coefficient
    con.close()
    if graph is True:
        lorenz(area, measures)[0].show()
    return gini_dict


def single_step_analysis(area, subarea, sim_distance="Distance"):
    """
    Returns a DataFrame with columns subarea, population, person meters,
    median distance, mean distance; ready for use in generating choropleth maps

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea category for analysis
    sim_distance(str): Distance column to be used

    Returns:
    results_df(pandas.DataFrame): DataFrame containing breakdown of population, person meters, mean and median distance
    """
    con = ps.db_exists(area)
    pragma = pd.read_sql_query("Pragma table_info(Postcodes)", con)
    columns = list(name[2] for name in pragma.itertuples())
    if subarea not in columns:
        log.error("%s is not a column within the database for %s", subarea, area)
        raise ValueError("%s is not a column within the database, must be one of %s" % (subarea, columns))
    else:
        results = {}
        query = """SELECT \"%s\"
                   FROM Postcodes
                   WHERE Population IS NOT NULL
                   AND \"%s\" IS NOT NULL""" % (subarea, subarea)
        subarea_df = pd.read_sql_query(query, con)
        subarea_df = subarea_df.drop_duplicates().values.tolist()
        sub_list = list(a[0] for a in subarea_df)
        results[subarea] = sub_list
        pm_list = []
        mean = []
        median = []
        populations = []
        for sub in sub_list:
            # Calculate total person meters
            query = """SELECT Population, \"%s\"
                       FROM Postcodes
                       WHERE \"%s\" = \"%s\"
                       AND Population IS NOT NULL""" % (sim_distance, subarea, sub)
            postcode_distance_df = pd.read_sql_query(query, con)
            pm_sum = 0
            pop_sum = 1
            distances = []
            for row in postcode_distance_df.itertuples():
                try:
                    pop = int(row[1])
                    dist = int(row[2])
                except ValueError:
                    continue
                pm_sum += dist*pop
                pop_sum += int(pop)
                dist_list = [dist] * pop
                for distance in dist_list:
                    distances.append(int(distance))
            populations.append(float(pop_sum/1000))
            pm_list.append(pm_sum)
            mean.append(float(pm_sum/(pop_sum*1000)))
            distance_array = np.array(distances, dtype=np.int64)
            try:
                median.append(float(np.median(distance_array)/1000))
            except ValueError:
                median.append(0)
        results["Population (thousands)"] = populations
        results["Person Meters"] = pm_list
        results["Mean Distance (km)"] = mean
        results["Median Distance (km)"] = median
        results_df = pd.DataFrame.from_dict(results)
        log.debug("Single step analysis completed for %s in %s", subarea, area)
        con.close()
        return results_df


def weighted_single_step(area, subarea, weightings, distance="Distance"):
    """
    Returns a DataFrame with columns subarea, population, person meters,
    median distance, mean distance; ready for use in generating choropleth maps.

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea category for analysis
    weightings(dict): keys=subareas, values=weighting for subarea
    distance(str): Distance column to be used

    returns:
    ss_df(pandas.DataFrame): dataframe with total person meters adjusted with weighting
    """
    ss_df = single_step_analysis(area, subarea, distance)
    weightings_df = pd.DataFrame.from_dict(weightings, orient="index")
    weightings_df.columns = ["Weighting"]
    weightings_df.index.name = subarea
    ss_df.merge(weightings_df, how="inner", on=subarea)
    ss_df = ss_df.merge(weightings_df, on=subarea, how="left")
    adjusted = []
    for row in ss_df.itertuples():
        if np.isnan(row[6]):
            weight = 1
        else:
            weight = row[6]
        aa_val = row[3] * weight
        adjusted.append(aa_val)
    ss_df["Adjusted Person Meters"] = adjusted
    return ss_df


def n_km(area, nkm, graph=False, distance="Distance", comparison=None):
    """
    Provides a count of individuals from within each n-km distance bracket.

    Parameters:
    area(str): Name of area to be studied
    nkm(int): Increment to be used (km)
    graph(bool): Generate bar graph displaying data if true
    distance(str): Distance column to be used
    comparison(str): Optional additional distance column

    Returns:
    results(dict): Dictionary of results per each n-km range
    """
    con = ps.db_exists(area)
    if comparison is not None:
        measures = [distance, comparison]
    else:
        measures = [distance]
    results_list = []
    for measure in measures:
        query = """SELECT Population, \"%s\"
                   FROM Postcodes
                   WHERE Population IS NOT NULL""" % measure
        population_distance_df = pd.read_sql_query(query, con)
        distances = []
        for row in population_distance_df.itertuples():
            distance = row[2]
            population = int(row[1])
            distance_enum = [distance] * population
            for value in distance_enum:
                try:
                    distances.append(int(value))
                except ValueError:
                    distances.append(10)
        distances_km = np.array(distances, dtype=np.int64)/1000
        max_dist = distances_km.max()
        results = {}
        lower = 0
        while lower < max_dist:
            upper = lower + nkm
            count = 0
            for d in distances_km:
                if lower < d <= upper:
                    count += 1
                else:
                    continue
            key = "%d to %d" % (lower, upper)
            results[key] = count
            lower += nkm
            continue
        results_list.append(results)
    if graph is True:
        width = 0.35
        m = -1
        n = 0
        for result in results_list:
            plt.bar(np.array(range(len(list(result.keys())))) + (m * width) / 2, list(result.values()),
                    width=width, label=measures[n])
            m = -m
            n += 1
            plt.xticks(range(len(list(result.keys()))), list(result.keys()), rotation="vertical")
        plt.ylabel("Number")
        plt.legend()
        plt.show()
    con.close()
    return results_list


def pop_by_center(area, graph=False, centre="Centre"):
    """
    Calculate the total population for each nearest centre.

    Parameters:
    area(str): Name of area to be studied
    graph(bool): True = generates a bar chart of data; False = no graph generated; default=False
    centre(str): Name of centre column to be used

    Returns:
    centre_population(dict): keys=Name of centre, values=Total number of people for whom that is there nearest centre
    """
    con = ps.db_exists(area)
    cur = con.cursor()
    cur.execute("SELECT Population, \""+centre+"\" FROM Postcodes").fetchall()
    centres_pc = pd.read_sql_query("SELECT \""+centre+"\" FROM Postcodes", con)
    centres_pc = centres_pc.drop_duplicates().values.tolist()
    centre_list = list(a[0] for a in centres_pc)
    centre_population = {}
    print(centre_list)
    for centre_pc in centre_list:
        query = "SELECT Population FROM Postcodes WHERE Population IS NOT NULL and "+centre+" = \"%s\"" % centre_pc
        pops = list(p[0] for p in cur.execute(query).fetchall())
        pops = np.array(pops)
        try:
            query = "SELECT Name From Hospitals WHERE Postcode = \"%s\"" % centre_pc
            centre_name, = cur.execute(query).fetchone()
        except:
            centre_name = centre_pc
        centre_population[centre_name] = pops.sum()
    con.close()
    if graph is True:
        plt.bar(centre_population.keys(), centre_population.values())
        plt.show()
    else:
        pass
    return centre_population
