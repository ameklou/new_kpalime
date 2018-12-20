from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

#from djgeojson.fields import PointField

class Category(models.Model):
    name=models.CharField(max_length=255)
    icon=models.ImageField(upload_to='icons')

    def __str__(self):
        return "category name {}".format(self.name)

class Place(models.Model):
    name = models.CharField(max_length=255)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    latitude=models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    longitude=models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    geom=models.PointField()
    #objects=models.GeoManager()

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.latitude  = self.geom['coordinates'][0]
    #     self.longitude = self.geom['coordinates'][1]
    #     super(Place, self).save(*args, **kwargs)
