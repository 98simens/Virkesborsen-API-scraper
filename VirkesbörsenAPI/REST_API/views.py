from django.shortcuts import render
from rest_framework import generics
from .serializers import AuctionItemGetAllSerializer, AuctionItemGetSpecificSerializer
from .models import AuctionItem
# Create your views here.

class ViewAll(generics.ListAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemGetAllSerializer

class ViewSpecific(generics.RetrieveAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemGetSpecificSerializer

        
