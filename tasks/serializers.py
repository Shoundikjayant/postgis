
from rest_framework_gis import serializers
from .models import Shop

class ShopSerializer(serializers.GeoModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
