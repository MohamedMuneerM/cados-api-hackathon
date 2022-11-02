from rest_framework import generics, filters

from . import models
from . import serializers


class AdvocateList(generics.ListAPIView):
    serializer_class = serializers.AdvocateSerializer
    queryset = models.Advocate.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    order_by = ['-id']
    search_fields = ['name', 'username']


class AdvocateRetreiveView(generics.RetrieveAPIView):
    lookup_field = 'username'
    model = models.Advocate
    serializer_class = serializers.AdvocateSerializer
    order_by = ['-id']
    queryset = models.Advocate.objects.all().order_by('-id')


