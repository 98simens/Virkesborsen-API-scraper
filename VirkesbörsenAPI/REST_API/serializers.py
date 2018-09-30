from rest_framework import serializers
from .models import AuctionItem

class AuctionItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuctionItem
        fields = ('auctionId', 'startBidingDate', 'endBidingDate', 'lat', 'long', 'data')
        read_only_fields = ('auctionId', 'startBidingDate', 'endBidingDate', 'lat', 'long', 'data')