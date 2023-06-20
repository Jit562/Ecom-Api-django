from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cardapp.models import *
from .serializers import *


# Create your views here.


class CartViews(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        '''
        Check the cart items
        ''' 
        user = request.user
        cart = Cart.objects.filter(user=user, order=False).first()
        query_set = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(query_set, many=True)

        return Response(serializer.data)

       
    def post(self, request, format=None):
        '''
        Add the cart items
        ''' 
        user = request.user
        data = request.data
        cart,_ = Cart.objects.get_or_create(user=user, order=False)
        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quentity = data.get('quentity')
        cart_items = CartItem(cart=cart, user=user, product=product, price=price, quentity=quentity)
        cart_items.save()

        '''
        update cart price on items quentity.
        '''
        total_price = 0
        cart_item = Cart.objects.filter(user=user, cart=cart.id)
        for items in cart_item:
            total_price += items.price
        cart.total_price = total_price
        cart.save()   

        return Response({'success':'Item added to your cart'})
    

        
    def put(self, request, format=None):
        '''
        Update the cart items
        ''' 
        data = request.data
        cart_item = CartItem.objects.get(id=data.get('id'))
        quentity = data.get('quentity')
        cart_item.quentity += quentity
        cart_item.save()

        return Response({'success':'Item Updated to your cart'})


    def delete(self, request, format=None):
        '''
        Delete the cart items
        ''' 
        data = request.data
        user = request.user

        cart_item = CartItem.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(user=user, order=False).first()
        query_set = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(query_set, many=True)

        return Response(serializer.data)
    


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        queryset = Orders.objects.filter(user=user)
        serializer = OrdersSerializer(queryset, many=True)

        return Response(serializer.data)    
