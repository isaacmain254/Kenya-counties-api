from django.shortcuts import render
from rest_framework import generics
from .models import County, Subcounty
from .serializers import CountySerializer, SubcountySerializer


class CountyList(generics.ListCreateAPIView):
    """
    A view for creating and listing all counties 
    """
    queryset = County.objects.all()
    serializer_class = CountySerializer


class CountyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete county details
    """
    serializer_class = CountySerializer
    # lookup_field = 'name'

    def get_object(self):
        county_name = self.kwargs.get('county_name')
        return County.objects.get(name=county_name)


class SubcountyList(generics.ListCreateAPIView):
    """
   A view for createing and listing subcounties
    """
    serializer_class = SubcountySerializer

    def get_queryset(self):
        county_name = self.kwargs.get('county_name')
        try:
            county = County.objects.get(name=county_name)
            return Subcounty.objects.filter(county=county)
        except County.DoesNotExist:
            return Subcounty.objects.none()

    def perform_create(self, serializer):
        county_name = self.kwargs.get('county_name')
        try:
            county = County.objects.get(name=county_name)
            serializer.save(county=county)
        except County.DoesNotExist:
            pass


class SubcountyDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting subcounty details
    """
    serializer_class = SubcountySerializer

    def get_object(self):
        subcounty_name = self.kwargs.get('subcounty_name')
        return Subcounty.objects.get(name=subcounty_name)
