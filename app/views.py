from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    