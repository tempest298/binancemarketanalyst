from binance.client import Client
import datetime
from Config.apiconf import API_KEY,API_SECRET
class CandleSticks():
    def __init__(self,pair,starttime,endtime,interval):
        cli = Client(API_KEY, API_SECRET) #interval should be CLIENT.KLINE_INTERVALXXXX
        ocp = cli.get_historical_klines(symbol=pair, interval=interval, start_str=starttime, end_str=endtime)
        self.Pair = pair
        self.Interval = interval
        self.StartTime = starttime
        self.EndTime = endtime
        self.Candles = []
        for kline in ocp:
            self.Candles.append(self.preparecandleobj(kline))

    def preparecandleobj(self,data):
        return Candle(data).__dict__
class Candle:
    def __init__(self,data):
        time = datetime.datetime.fromtimestamp(int(data[0]) / 1000)
        splt = str(time).split(' ')
        timec = datetime.datetime.fromtimestamp(int(data[6]) / 1000)
        spltc = str(timec).split(' ')
        self.OpenDate = splt[0]
        self.OpenTime = splt[1]
        self.CloseDate = spltc[0]
        self.CloseTime = spltc[1]
        self.CandleMainTop = data[1]
        self.CandleTop = data[2]
        self.CandleMainBot = data[4]
        self.CandleBot = data[3]
        self.CandleVolume = data[5]
        self.CandleTradesCount = data[8]