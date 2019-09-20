from synctrades import TradeHistory as TradeHistory
from binance.client import Client
import datetime
from Config.apiconf import API_KEY,API_SECRET
from binance.websockets import BinanceSocketManager
from Config.handledpairs import Pair
from Threading.threadcreator import ThreadHandler
from opencloseprice import CandleSticks
from cachedb import CacheDatabase
import time
from depth import Depth
import candlelistener
CacheDB = CacheDatabase()

#OAXBTC = ThreadHandler(TradeHistory,Pair.OAXBTC.value)
#OAXBTC.StartThread()
#BNBBTC = ThreadHandler(TradeHistory,Pair.BNBBTC.value).StartThread()
#oax = TradeHistory(Pair.OAXBTC.value)
cli = Client(API_KEY, API_SECRET)

from algorithms.depthanalyze import DepthAnalyze

DepthAnalyze(Pair.OAXBTC.value)


