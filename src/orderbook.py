from binance.client import Client
from Config.apiconf import API_KEY,API_SECRET
class Market():
    def __init__(self,Pair):
        cli = Client.get_ticker(symbol=Pair)
        self.Pair = Pair
        self.dailyHight = cli['highPrice']
        self.dailyLow = cli['lowPrice']
        self.dailyBTCVol = cli['quoteVolume']
        self.dailyPriceChange = cli['priceChange'] # satoshi price change
        self.dailyPriceChangePercent = cli['priceChangePercent']



