import threading
from opencloseprice import CandleSticks
from cachedb import CacheDatabase
import json
def candleListener(candle,updatetime):
    timer = threading.Timer(updatetime*2,candlehandler,args=(candle,))
    timer.start()

def candlehandler(candle):
    newcnd = CandleSticks(candle.Pair,candle.StartTime,candle.EndTime,candle.Interval)
    CacheDB = CacheDatabase.getInstance()
    candobj = {}
    candobj[newcnd.Pair] = newcnd.Candles
    print(newcnd.Candles)
    if CacheDB.isKeySet("Candles"):
        x = CacheDB.getObject("Candles")
        index = -1
        for i in range(len(x)):
            if newcnd.Pair in list(x[i].keys()):
                print("inlst")
                del x[i]

        x.append(candobj)
        CacheDB.setObject("Candles",x)
    else:
        x = []
        x.append(candobj)
        CacheDB.setObject("Candles",x)
    print("{} Pair's candles updated on CacheDB".format(newcnd.Pair))
    print(json.dumps(CacheDB.getDatabase()))