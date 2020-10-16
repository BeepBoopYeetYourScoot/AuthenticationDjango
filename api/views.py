from rest_framework_json_api import views
from . import models, serializers
import requests
from django.shortcuts import redirect
from rest_framework.response import Response


class FarmViewSet(views.ModelViewSet):
    queryset = models.Farm.objects.all()
    serializer_class = serializers.FarmSerializer


class CatViewSet(views.ModelViewSet):
    queryset = models.CatModel.objects.all()
    serializer_class = serializers.CatSerializer


class OwnerViewSet(views.ModelViewSet):
    queryset = models.HomeOwner.objects.all()
    serializer_class = serializers.OwnerSerializer


class FarmRelationshipView(views.RelationshipView):
    queryset = models.Farm.objects
    self_link_view_name = 'farms-relationships'


class CatRelationshipView(views.RelationshipView):
    queryset = models.CatModel.objects
    self_link_view_name = 'cats-relationships'


class OwnerRelationshipView(views.RelationshipView):
    queryset = models.HomeOwner.objects
    self_link_view_name = 'owners-relationships'
