from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_inquiry, name='order_inquiry'),
]