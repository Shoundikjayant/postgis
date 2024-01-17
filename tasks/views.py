# views.py
from rest_framework import generics
from .models import Shop
from .serializers import ShopSerializer

class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
# serializers.py