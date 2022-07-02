#example:
example = [11,345,516,323,324,47,832,6,22,134,82,16,44,53]

from indipy import *
test = {
    'INPUT' : example,
    'SMA' : sma(example,3),
    'STOCH RSI' : stoch(rsi(example,3),3),
    'RSI' : rsi(example,3),
    'SD' : sd(example,3),
    'BB' : bb(example,3),
    'EMA' : ema(example,3)
}

from tabulate import tabulate
tab = lambda x : tabulate(x,tablefmt = 'presto',headers = list(x.keys()))
print(tab(test))
