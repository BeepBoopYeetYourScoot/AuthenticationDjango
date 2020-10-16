from rest_framework_json_api import serializers
from . import models
from rest_framework_json_api import relations


class FarmSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Farm
        fields = '__all__'

    owned_cats = relations.ResourceRelatedField(
        model=models.CatModel,
        many=True,
        required=False,
        queryset=models.CatModel.objects.all(),
        related_link_view_name='farms-related'
    )

    farm_owner = relations.ResourceRelatedField(
        model=models.HomeOwner,
        many=False,
        required=False,
        queryset=models.HomeOwner.objects.all(),
        self_link_view_name='farms-relationships',
        related_link_view_name='farms-related'
    )

    included_serializers = {'owned_cats': 'api.serializers.CatSerializer',
                            'farm_owner': 'api.serializers.OwnerSerializer'}


class CatSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.CatModel
        fields = '__all__'

    farm = relations.ResourceRelatedField(
        model=models.Farm,
        many=False,
        required=False,
        queryset=models.Farm.objects.all(),
        self_link_view_name='cats-relationships',
        related_link_view_name='cats-related'
    )

    included_serializers = {'farm': 'api.serializers.FarmSerializer'}


class OwnerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.HomeOwner
        fields = '__all__'

    owned_shelters = relations.ResourceRelatedField(
        model=models.Farm,
        many=True,
        required=False,
        queryset=models.Farm.objects.all(),
        related_link_view_name='owners-related'
    )

    included_serializers = {'owned_shelters': 'api.serializers.FarmSerializer'}
