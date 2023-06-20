from django.shortcuts import render

from ecom.serializers import ProductSerializer

from ecom.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ProductView(APIView):

    """
    List all Products, or create a new products.
    """

    def get(self, request, format=None):

        category = self.request.query_params.get('category')

        if category:
            queryset = Product.objects.filter(category__category_name = category)

        else:
            queryset = Product.objects.all()

        serializer = ProductSerializer(queryset, many = True)

        return  Response({'count': len(serializer.data), 'data': serializer.data}) 
    

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

