from rest_framework import serializers
from .models import County, Subcounty


class CountySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='county-detail', lookup_field='name', lookup_url_kwarg='county_name')
    sub_counties = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = County
        fields = ['url', 'name', 'code', 'logo',
                  'capital', 'population', 'sub_counties']


class SubcountySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subcounty
        fields = ['name', 'population']
