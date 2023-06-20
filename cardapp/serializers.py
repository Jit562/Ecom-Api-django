from rest_framework.serializers import ModelSerializer

from cardapp.models import *

from ecom.serializers import *




class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()
    cart = CartSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'



class OrdersSerializer(ModelSerializer):
    cart = CartSerializer()
    class Meta:
        model = Orders
        fields = '__all__'        