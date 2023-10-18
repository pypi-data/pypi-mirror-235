"""
    Module containing code necessary for creation of choropleth maps in javascript leaflets, using folium

"""

import logging as log
import sqlite3
import geopandas as gpd
import folium
from folium.plugins import HeatMap
import pandas as pd
import geoserv.analyse as analyse


def auto_centre(area, centres):
    """
    Calculates the centre-point of the centres used in the analysis to later create a map centred around this point.

    Parameters:
    area(str): Name of area to be studied
    centres(list): List of postcodes for the centres to be used in the analysis

    return:
    centre_point(list): latitude, longitude pair for the centroid of the centres used

    """
    con = sqlite3.connect(area + ".sqlite")
    cur = con.cursor()
    lat_sum = 0
    lon_sum = 0
    no_centres = 0
    if isinstance(centres, list) is True:
        for centre in centres:
            query = "SELECT Latitude, Longitude FROM Postcodes WHERE Postcode=\"%s\"" % centre
            geom = cur.execute(query).fetchone()
            lat_sum += geom[0]
            lon_sum += geom[1]
            no_centres += 1
    else:
        raise TypeError("Postcodes must be given as a string or list of strings")
    centre_point = [lat_sum/no_centres, lon_sum/no_centres]
    return centre_point


def choropleth(area: object, subarea: object, boundaries: object, metric: object = "Person Meters", name: object = "name", centres: object = None, weighting: object = False,
               distance: object = "Distance", file_type: object = "geojson", ex_data: object = None) -> object:
    """
    Creates html file for Choropleth map, with a separate layer for each metric stored in the dataframe,
    and a centre marker layer.

    Parameters:
    area(str): Name of area to be studied
    subarea(str): Name of subarea category for analysis
    metric(str): Name of metric to be used. Must be one of "Person Meters", "Population (thousands)",
                 "Mean Distance (km)", "Median Distance (km)", unless using external data
    centres(list): Default None; List of postcodes (including spaces) for the centres to be used. If None is passed, a
                   standard centre point in the UK will be used instead
    boundaries(str): Default None; Name of shapefile containing boundary data excluding .shp suffix. If None is passed,
                     it is assumed that the files share the same name as the area parameter
    weighting(dict): Dictionary of weightings to be used.
    distance(str): Name of distance column to be used
    file_type(str): File type for boundary data. Must be either "geojson" or "shp"
    ex_data(dict): External data to be visualised on choropleth map, format {index: (subarea, value)}

    Returns:
    None
    """
    if boundaries is None:
        boundaries = subarea
    else:
        pass
    if centres is None:
        # Default centre position
        area_map = folium.Map([55.9533, -3.1883], zoom_start=6)
    else:
        # Auto centre map on centroid of centres
        area_map = folium.Map(auto_centre(area, centres), zoom_start=6)
    folium.TileLayer('cartodbpositron').add_to(area_map)
    key = "feature.properties.%s" % subarea
    geo_df = gpd.read_file(boundaries + "." + file_type)
    geo_df['coords'] = geo_df['geometry'].apply(lambda x: x.representative_point().coords[:])
    geo_df['coords'] = [coords[0] for coords in geo_df['coords']]
    geo_df.rename(columns={name: subarea}, inplace=True)
    if weighting is False:
        data_df = analyse.single_step_analysis(area, subarea, distance)
        tooltips = [subarea, "Population (thousands)", "Person Meters", "Mean Distance (km)",
                    "Median Distance (km)"]
    else:
        data_df = analyse.weighted_single_step(area, subarea, weighting, distance)
        tooltips = [subarea, "Population (thousands)", "Person Meters", "Mean Distance (km)",
                    "Median Distance (km)", "Adjusted Person Meters"]
    if ex_data is not None:
        ex_comp_df = pd.DataFrame.from_dict(ex_data, orient="index", columns=[subarea, metric])
        data_df = data_df.merge(ex_comp_df, on=subarea)
        tooltips.append(metric)
    else:
        pass
    geo_merge = geo_df.merge(data_df, on=subarea, how='left')
    geo_merge = geo_merge.dropna(subset=[metric])
    choropleth_map = folium.Choropleth(geo_data=geo_merge,
                                       name=metric,
                                       data=data_df,
                                       columns=[subarea, metric],
                                       key_on=key,
                                       fill_color="BuPu",
                                       fill_opacity=0.7,
                                       line_opacity=0.2,
                                       highlight=True).add_to(area_map)
    folium.GeoJsonTooltip(tooltips).add_to(choropleth_map.geojson)
    if centres is None:
        pass
    else:
        centre_group = folium.FeatureGroup("Centres")
        for centre in centres:
            folium.CircleMarker(location=(centre[1], centre[2]),
                                popup=centre[0],
                                radius=5).add_to(centre_group)
        centre_group.add_to(area_map)
    folium.LayerControl().add_to(area_map)
    area_map.save("%s_%s_%s_%s.html" % (area, subarea, metric, distance))
    log.info("Choropleth map created for %s in %s", subarea, area)


def heatmap(area, centres=None, metric="person meters", distance="Distance"):
    con = sqlite3.connect(area + ".sqlite")
    cur = con.cursor()
    if centres is None:
        # Default centre position
        hmap = folium.Map([55.9533, -3.1883], zoom_start=6)
    else:
        # Auto centre map on centroid of centres
        hmap = folium.Map(auto_centre(area, centres), zoom_start=6)
    folium.TileLayer('cartodbpositron').add_to(hmap)
    query = """SELECT Latitude, Longitude, Population, \"%s\" 
               FROM Postcodes 
               WHERE Distance IS NOT NULL and Population IS NOT NULL""" % distance
    data_df = pd.read_sql_query(query, con)
    values = []
    if metric == "person meters":
        for row in data_df.itertuples():
            values.append(float(row[3] * row[4]))
    elif metric == "population":
        for row in data_df.itertuples():
            values.append(float(row[3]))
    elif metric == "distance":
        for row in data_df.itertuples():
            values.append(float(row[4]))
    else:
        raise ValueError("Metric must be either \"person meters\" or \"population\" or \"distance\"")
    data_df["PM"] = values
    data_max = data_df["PM"].max()
    hmap = folium.Map(location=[55.9533, -3.1883], zoom_start=6)
    hm_wide = HeatMap(list(zip(data_df.Latitude.values, data_df.Longitude.values, data_df.PM.values)),
                      name=metric,
                      min_opacity=0.4,
                      max_val=data_max,
                      radius=10, blur=15,
                      max_zoom=1)
    hmap.add_child(hm_wide)
    if centres is None:
        pass
    else:
        centre_group = folium.FeatureGroup("Neurosurgery Centres")
        for centre in centres:
            geom = cur.execute("""SELECT Latitude, Longitude
                                  FROM Postcodes
                                  WHERE Postcode=?""", (centre,)).fetchone()
            folium.CircleMarker(location=(geom[0], geom[1]),
                                radius=5).add_to(centre_group)
        centre_group.add_to(hmap)
    folium.LayerControl().add_to(hmap)
    hmap.save("%s_heatmap_%s_%s.html" % (area, metric, distance))
    con.close()
