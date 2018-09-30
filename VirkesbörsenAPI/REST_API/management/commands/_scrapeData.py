from bs4 import BeautifulSoup as bfs
import requests as rq
from urllib.parse import urljoin
import locale
from datetime import datetime

class WebScraper:
    def __init__(self, url, page, signInUrl, email, password):
        self.url = url
        self.targetPage = urljoin(url, page)

        #Start Session
        self.session = rq.Session()
        
        #Get page
        self.getRequest = self.session.get(self.targetPage)

        #Check ok response
        self.getRequest.raise_for_status()
        
        self.bfs = bfs(self.getRequest.text, features='html5lib')

        #Sign in
        loginUrl = urljoin(url,signInUrl)
        self.session.get(loginUrl)
        csrfToken = self.session.cookies.get_dict()['csrftoken']
        form_data = {'email':email, 'password':password, 'csrfmiddlewaretoken':csrfToken}
        self.session.post(loginUrl, data=form_data, headers={'Referer':loginUrl})

    def getAuctionLinks(self):
        #loop through link tags with css class thelink, return all hrefs from matched link tags
        return (auction_elem['href'] for auction_elem in self.bfs.find_all('a', class_='thelink'))
    
    def getAuctionItems(self):
        auctionDataItems = []
        #Loop through each found auction
        for link in self.getAuctionLinks():
            #Get auction html adn make BeautifulSoup object
            auctionUrl = urljoin(self.url, link)
            auctionRequest = self.session.get(auctionUrl)
            auctionBfs = bfs(auctionRequest.text, features='html5lib')

            #Scrape key values from BeautifulSoup object
            auctionId = auctionBfs.find('span', attrs={'data-id': True})['data-id']
            auctionStartDate = auctionBfs.select_one('div.details > div:nth-of-type(1) > div:nth-of-type(2)').getText().strip()
            auctionEndDate = auctionBfs.select_one('div.details > div:nth-of-type(2) > div:nth-of-type(2)').getText().strip()
            auction_lat_long = auctionBfs.select_one('a.btn.map')["href"].split("/")[-1].split(",")

            #Scrape Remaning data objects into Dictionary
            auction_data = {}
            for detail in auctionBfs.select('div.details > div'):
                if(detail.has_attr("class")):
                    continue
                children = detail.findAll("div", recursive=False)
                name = children[0].getText().strip()
                value = children[1].getText().strip()
                auction_data[name] = value

            #Create new dict with add data, convert dates into datetime objects, add to result list
            locale.setlocale(locale.LC_ALL, 'sv_SE')
            auctionDataItems.append({
                'auctionId': auctionId,
                'startBidingDate': datetime.strptime(auctionStartDate, '%d %B %Y'),
                'endBidingDate': datetime.strptime(auctionEndDate, '%d %B %Y'),
                'lat': float(auction_lat_long[0]),
                'long': float(auction_lat_long[1]),
                'data': auction_data
            })
        return auctionDataItems