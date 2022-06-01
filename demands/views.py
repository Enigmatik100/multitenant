from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Demand
from .serializer import DemandSerializer


class ListCreateDemand(generics.ListCreateAPIView):
    serializer_class = DemandSerializer
    queryset = Demand.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)
