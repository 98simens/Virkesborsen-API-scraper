from django.test import TestCase
from .models import AuctionItem
import datetime
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# Create your tests here.


class ModelTestCase(TestCase):

    def setUp(self):
        self.auctionItem = AuctionItem(
            auctionId = 300,
            startBidingDate = datetime.datetime.now(),
            endBidingDate = datetime.datetime.now(),
            lat=57.701946,
            long=13.183594,
            data = {"Åtgärd": "Slutavverkning", "Kontrakttyp": "Leveransrotpost"}
        )
    
    def testModelCanCreateAuctionItem(self):
        beforeCount = AuctionItem.objects.count()
        self.auctionItem.save()
        afterCount = AuctionItem.objects.count()
        self.assertNotEqual(beforeCount, afterCount)

class ApiTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.auctionItem = AuctionItem(
            auctionId = 300,
            startBidingDate = datetime.datetime.now(),
            endBidingDate = datetime.datetime.now(),
            lat=57.701946,
            long=13.183594,
            data = {"Åtgärd": "Slutavverkning", "Kontrakttyp": "Leveransrotpost"}
        )
        self.auctionItem.save()
        self.response = self.client.get(
            reverse('getAll')
        )
    
    def test_api_get(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)