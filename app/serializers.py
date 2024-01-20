from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, IntegerField,Serializer,  CharField, DecimalField
from django.db.models import Q

from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CreateProductSerializer(Serializer):
    
    PROD = None

    category = IntegerField()
    name = CharField()
    price = DecimalField(max_digits=10, decimal_places=2)
    off = IntegerField()
    qty = IntegerField()

    # class Meta:
    #     model = Product
    #     fields = ['name','price','qty', 'off', 'category']

    def validate(self, attrs):
        category_id = attrs.get('category')
        name = attrs.get('name')
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError("category is not found", code=status.HTTP_400_BAD_REQUEST)
        if category:
            db_cat_prod = CategoryProduct.objects.filter(Q(product__name=name) & Q(category=category)).first()
            if db_cat_prod:
                raise ValidationError(f"category {category_id}  already have product with this name", code=400)
        
        return super().validate(attrs)

    def create(self, validated_data):
        name = validated_data.get('name')
        price = validated_data.get('price')
        off = validated_data.get('off')
        category = Category.objects.get(id= validated_data.get('category'))
        qty = validated_data.get('qty')
        product = Product.objects.create(name=name,
                                         price=price,
                                         qty=qty,
                                         off=off)
        return CategoryProduct.objects.create(category=category, product=product)
        
        