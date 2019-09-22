from django.shortcuts import render

class MyApi(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        external_api_url = ""
        res = urllib.urlopen(external_api_url).read()
        data = json.loads(res)
        return Response(data, status=HTTP_200_OK)

import json
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
from .models import Person
from .serializers import PersonSerializer


class PersonView(APIView):

    def get(self, request):
        data = urlopen("<JSONURLHERE>").read()
        output = json.loads(data)
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        for person in output:
            if person['id'] not in [i.id for i in persons]:
                Person.objects.create(id=person['id'], name=person['name'], image_url=person['image_url'],
                                          title=person['title'], bio=person['bio'])
        return Response(serializer.data)
