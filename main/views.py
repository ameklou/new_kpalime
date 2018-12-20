from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Place
from django.core.serializers import serialize
from django.http import HttpResponse
# Create your views here.

class HomePageView(TemplateView):
    template_name='main/index.html'


def datas(request):
    datas=serialize('geojson',Place.objects.all())
    return HttpResponse(datas,content_type="json")
