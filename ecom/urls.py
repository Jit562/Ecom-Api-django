from django.urls import path
from ecom.views import *

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
]