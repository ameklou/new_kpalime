from django.contrib import admin
from .models import Place,Category
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class PlaceAdmin(LeafletGeoAdmin):
    readonly_fields=('longitude','latitude',)
admin.site.register(Place,LeafletGeoAdmin)
admin.site.register(Category)
