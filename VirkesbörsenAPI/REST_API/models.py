from django.db import models
from django.contrib.postgres.fields import HStoreField, ArrayField

# Create your models here.

class AuctionItem(models.Model):
    auctionId = models.IntegerField(primary_key=True, unique=True)
    startBidingDate= models.DateField(help_text="format yyyy-MM-dd", null=True)
    endBidingDate = models.DateField(help_text="format yyyy-MM-dd")
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)

    data = HStoreField()

    def __str__(self):
        return str(self.auctionId)