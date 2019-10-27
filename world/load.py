import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, LINKStation, linkstation_mapping

# world border
world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS', 'TM_WORLD_BORDERS-0.3.shp'),
)

def run_worldborder(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

# link station
link_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'LINK_stations', 'LINK_stations.shp'),
)

def run_linkstation(verbose=True):
    lm = LayerMapping(LINKStation, link_shp, linkstation_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
