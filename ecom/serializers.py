from rest_framework import serializers
from ecom.models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('created_at','updated_at')



class ColorVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = ColorVariant
        exclude = ('id','created_at','updated_at')


class SizeVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = SizeVariant
        exclude = ('id','created_at','updated_at')



class QuantityVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuantityVariant
        exclude = ('id','created_at','updated_at')


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    quentity_type = QuantityVariantSerializer()
    color_type = ColorVariantSerializer()
    size_type = SizeVariantSerializer()
    
    class Meta:
        model = Product
        fields = '__all__'