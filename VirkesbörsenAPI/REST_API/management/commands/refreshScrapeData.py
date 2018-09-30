from django.core.management.base import BaseCommand
from ._scrapeData import WebScraper
from REST_API.models import AuctionItem
import config

class Command(BaseCommand):
    help = 'Refresh scrape data in database'
    def handle(self, *args, **kwargs):
        scraper = WebScraper('https://www.virkesborsen.se', '/auctions/', '/login/', config.EMAIL, config.PASSWORD)
        auctionDataItems = scraper.getAuctionItems()
        for auctionData in auctionDataItems:
            AuctionItem.objects.update_or_create(auctionData, auctionId=auctionData['auctionId'])
