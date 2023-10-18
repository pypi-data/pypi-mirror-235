from setuptools import setup

setup(name="geoserv",
      version="0.0.2",
      description="Service distribution equality analysis tool",
      author="Kieran Johnstone",
      author_email="krj15@ic.ac.uk",
      Packages=[],
      install_requires=["osmnx", "networkx", "pandas", "sqlite3", "igraph",
                        "numpy", "matplotlib", "geopandas", "folium", "dash"]
      )
