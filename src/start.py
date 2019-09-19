from binance.client import Client
from Config.apiconf import API_KEY,API_SECRET
import datetime
import pandas as pd
cli = Client(API_KEY,API_SECRET)
depth = cli.get_order_book(symbol='OAXBTC')
prices = cli.get_ticker(symbol="OAXBTC")
recent_trades = cli.get_recent_trades(symbol="OAXBTC")
pd.set_option('display.max_rows',None)
print(recent_trades)
new_trades = []
for trade in recent_trades:
    del trade['isBestMatch']
    if trade['isBuyerMaker']:
        trade['type'] = 'SELL'
    else:
        trade['type'] = 'BUY'
    del trade['isBuyerMaker']
    time = datetime.datetime.fromtimestamp(int(trade['time'])/1000)
    splt = str(time).split(' ')
    trade['date'] = splt[0]
    trade['time'] = splt[1].split('.')[0]
    new_trades.append(trade)
pdf = pd.DataFrame(new_trades).sort_values(by='id',ascending=False) # data frame sorted with trade id
print(pdf)