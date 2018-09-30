from django.shortcuts import render
from rest_framework import generics
from .serializers import AuctionItemSerializer
from .models import AuctionItem
# Create your views here.

class ViewAll(generics.ListAPIView):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionItemSerializer
