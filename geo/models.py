from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    lat_lon = models.PointField(geography=True, default='POINT(0.0 0.0)')

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


# This is an auto-generated Django model module created by ogrinspect.
class LINKStation(models.Model):
    objectid = models.BigIntegerField()
    name = models.CharField(max_length=80, serialize='Name')
    latitude = models.FloatField()
    longitude = models.FloatField()
    field4 = models.CharField(max_length=80)
    geom = models.PointField(srid=4326)


# Auto-generated `LayerMapping` dictionary for LINKStation model
linkstation_mapping = {
    'objectid': 'OBJECTID',
    'name': 'Name',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'field4': 'Field4',
    'geom': 'POINT',
}

