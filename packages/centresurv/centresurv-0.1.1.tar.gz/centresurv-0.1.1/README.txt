Centresurv 0.1.2
---------

Geoserv is a python package that allows for the easy assessment of distribution of services in an area.
It also allows for easy integration with population distribution data.

---------

DEPENDENCIES:

osmnx, networkx, pandas, sqlite3, python_igraph, numpy, matplotlib, geopandas, folium

Installation of osmnx, igraph and geopandas via pip is often problematic, particularly on Windows OS. It may be possible
to do so using conda, or to manually install from the wheelfiles, as shown in this tutorial:
https://geoffboeing.com/2014/09/using-geopandas-windows/

N.B. If following this method for installation of geopandas, it is then possible to simply pip install osmnx

Alternatively, it may be more convenient to use windows subsystem for linux.
---------

Geoserv consists for four main modules:

postcode_setup -> This module contains all the functions required to import and save a graph for a given area of
                  interest, taking the map data from the Open Street Map APIs.

                  Given a csv file containing postcode data for the same area (for the UK available from:
                  https://www.doogal.co.uk/), a database can be created and shortest path analysis performed.

analyse -> This contains functions to calculate very basic statistics regarding the shortest path analysis completed
           such as average distances, total person-meters in an area, and the gini coefficient for the entire area

maps -> This uses the data generated in the analyse module to create high quality visualisations of the data on
        choropleth maps using folium, and saves these as html files. The boundaries for use in this must be downloaded
        as shapefiles (for UK these are available from: http://geoportal.statistics.gov.uk/ or https://data.gov.uk/)

        N.B. The shapefiles used must have a column entitled "name" containing the same sub-area names as are found in
             the database. It is likely that these will require some degree of cleaning in order to match

---------
ACKNOWLEDGEMENTS:

This package builds upon and integrates the functionality of several much better packages. Much of the
functionality represents only small incremental modifications on the dependencies listed above, in particular osmnx.
