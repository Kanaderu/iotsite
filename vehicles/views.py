from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'vehicles/index.html', {})

def vehicles(request, vehicles):
    return render(request, 'vehicles/room.html', {
        'vehicles_json': mark_safe(json.dumps(vehicles))
    })
