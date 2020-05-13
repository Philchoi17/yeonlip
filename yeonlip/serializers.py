from rest_framework import serializers

from core.models import Yeonlip, Unit


class YeonlipSerializer(serializers.ModelSerializer):
    """Serializer for yeonlip objects"""

    class Meta:
        model = Yeonlip
        fields = (
            'id', 'full_addr', 'dong_addr', 'road_addr', 'bldg_nm',
            'land_area', 'base_area', 'total_area', 'struct_name',
            'struct_others','main_use', 'other_use', 'roof_name',
            'roof_others', 'height', 'above_floors', 'under_floors',
            'passenger_elev', 'emergency_elev', 'land_price_m2',
            'area_usage', 'x', 'y', 'constr_date', 'est_price_m2',
            'est_price'
        )
        read_only_fields = ('id',)


class UnitSerializer(serializers.ModelSerializer):
    """Serializer for unit objects"""
    yeonlip_building = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Yeonlip.objects.all()
    )

    class Meta:
        model = Unit
        fields = (
            'id', 'area', 'block_name', 'floor_number', 'floor_type_code',
            'floor_type_name', 'unit_name', 'est_price', 'est_price_m2',
            'yeonlip_building'
        )
        read_only_fields = ('id',)
