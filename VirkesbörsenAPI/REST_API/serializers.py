from rest_framework import serializers
from .models import AuctionItem

class AuctionItemGetAllSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuctionItem
        fields = ('auctionId', 'startBidingDate', 'endBidingDate', 'lat', 'long')
        read_only_fields = fields

class AuctionItemGetSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionItem
        fields = ('auctionId', 'startBidingDate', 'endBidingDate', 'lat', 'long', 'data')
        read_only_fields = fields