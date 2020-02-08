import json
from djgeojson.serializers import Serializer
from django.http import JsonResponse
from .models import LINKStation


class GeoJSONSerializer(Serializer):

    # Modify serializer to remove 'crs' from the root and 'id' from each feature
    # as this breaks the ArcGIS api when rendering
    def serialize(self, queryset, **options):
        res = super().serialize(queryset, **options)
        json_res = json.loads(res)
        json_res.pop('crs', None)

        [feature.pop('id', None) for feature in json_res['features']]

        return json_res


def GeoJSONLinkStations(request):
    link_stations = GeoJSONSerializer().serialize(LINKStation.objects.all(), crs=False, properties=('name',), use_natural_keys=True, with_modelname=False)

    return JsonResponse(link_stations)
