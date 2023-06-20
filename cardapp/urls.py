from django.urls import path
from cardapp.views import *

urlpatterns = [
    path('cart/', CartViews.as_view(), name='cart'),
    path('order/', OrderView.as_view(), name='order'),
]