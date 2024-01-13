from django.urls import path, include
from rest_framework import routers
from .views import ProductView

router  = routers.DefaultRouter()
router.register(r'product', ProductView, )

urlpatterns = [
    path('', include(router.urls))
]