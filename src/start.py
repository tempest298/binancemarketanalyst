from synctrades import TradeHistory as TradeHistory
from binance.client import Client
import datetime
from Config.apiconf import API_KEY,API_SECRET
from binance.websockets import BinanceSocketManager


x = TradeHistory('XEMBTC')
print(x.getTrades())
