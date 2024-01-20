from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class ProductView(CreateAPIView):
    serializer_class = CreateProductSerializer
    queryset = Product.objects.all()

    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()    
       
        
        return Response({"msg":'dsd'})


