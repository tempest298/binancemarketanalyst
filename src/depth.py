from binance.client import Client
from Config.apiconf import API_KEY,API_SECRET
import datetime
from binance.websockets import BinanceSocketManager
import pandas as pd
class Depth:
    def __init__(self,pair,callback_diff,callback_partial):
        cli = Client(API_KEY, API_SECRET)
        bm = BinanceSocketManager(cli)
        diff_key = bm.start_depth_socket(pair, callback_diff)
        partial_key = bm.start_depth_socket(pair, callback_partial, depth=BinanceSocketManager.WEBSOCKET_DEPTH_10)
        bm.start()