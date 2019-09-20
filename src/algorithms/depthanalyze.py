from depth import Depth
class DepthAnalyze:
    def __init__(self,pair):
        dp = Depth(pair,self.DiffHandler,self.PartialHandler)
        self.BestBidPrc = 0
        self.BestBidQty = 0
        self.BestAskPrc = 0
        self.BestAskQty = 0
        self.Pair = pair
    def DiffHandler(self,data):
        for bid in data['b']:
            print("Bid Price changed: Price : {}, Qty : {}".format(bid[0],bid[1]))
        for ask in data['a']:
            print("Ask Price changed: Price : {}, Qty : {}".format(ask[0],ask[1]))


    def PartialHandler(self,data):
        print("msg on partial {}".format(data))
        self.BestBidPrc = data['bids'][0][0]
        self.BestBidQty = data['bids'][0][1]
        self.BestAskPrc = data['asks'][0][0]
        self.BestAskQty = data['asks'][0][1]
        self.BestBids = data['bids']
        self.BestAsks = data['asks']
        print(self.BestBidPrc)
