from binance.client import Client
from Config.apiconf import API_KEY,API_SECRET
import datetime
from binance.websockets import BinanceSocketManager
import pandas as pd
from cachedb import CacheDatabase
class TradeHistory():
    def __init__(self, Pair):
        cli = Client(API_KEY, API_SECRET)
        pd.set_option('display.max_rows', None)
        recent_trades = cli.get_recent_trades(symbol=Pair)
        new_trades = []
        for trade in recent_trades:
            del trade['isBestMatch']
            if trade['isBuyerMaker']:
                trade['type'] = 'SELL'
            else:
                trade['type'] = 'BUY'
            del trade['isBuyerMaker']
            del trade['quoteQty']
            time = datetime.datetime.fromtimestamp(int(trade['time']) / 1000)
            splt = str(time).split(' ')
            trade['date'] = splt[0]
            trade['time'] = splt[1].split('.')[0]
            new_trades.append(trade)
        pdf = pd.DataFrame(new_trades).sort_values(by='id', ascending=True)
        self.Trades = pdf
        self.Pair = Pair
        bm = BinanceSocketManager(cli)
        conn_key = bm.start_trade_socket(Pair, self.SyncTrades)
        bm.start()
        print("{}'s trades are started to listening.".format(Pair))
        self.isListening = True

    def getTrades(self):
        return self.Trades

    def SyncTrades(self,msg):
        del msg['e']
        del msg['s']
        if msg['m']:
            msg['type'] = 'SELL'
        else:
            msg['type'] = 'BUY'
        del msg['b']
        del msg['E']
        del msg['a']
        del msg['m']
        time = datetime.datetime.fromtimestamp(int(msg['T']) / 1000)
        splt = str(time).split(' ')
        msg['date'] = splt[0]
        msg['time'] = splt[1].split('.')[0]
        del msg['T']
        del msg['M']
        msg['id'] = msg['t']
        msg['price'] = msg['p']
        del msg['t']
        del msg['p']
        msg['qty'] = msg['q']
        del msg['q']
        temp_df = pd.DataFrame(msg,index=[0],columns=self.Trades.columns)
        self.Trades = self.Trades.append(temp_df,ignore_index=True).sort_values(by='id',ascending=True)
        CacheDatabase.setObject()
        print("{0} trade added to list \n {1}".format(self.Pair,temp_df))