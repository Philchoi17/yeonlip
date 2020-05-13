from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, generics
from rest_framework.permissions import IsAuthenticated

from core.models import Yeonlip, Unit

from yeonlip import serializers


class YeonlipViewSet(viewsets.ModelViewSet):
    """Manage yeonlip list"""
    serializer_class = serializers.YeonlipSerializer
    queryset = Yeonlip.objects.all()
#    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """listing yeonlip buildings"""
        
        print(self.request.GET)
        return Yeonlip.objects.filter(full_addr__contains=self.request.GET['full_addr'])


class UnitViewSet(viewsets.ModelViewSet):
    """Manage Units in the db"""
    serializer_class = serializers.UnitSerializer
    queryset = Unit.objects.all()
#    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the units for the associated yeonlip building"""
        return Unit.objects.filter(yeonlip_building=self.request.GET['building_id'])
