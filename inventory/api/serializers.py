from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'pd_name' , 'pd_type' , 'pd_cost' , 'pd_count']