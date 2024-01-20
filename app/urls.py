from django.urls import path, reverse, resolve, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('category', CategoryView, basename="category" )

urlpatterns = [
    path('product', ProductView.as_view(), name='product'),
    path('', include(router.urls))
]