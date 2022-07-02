####################################################################
#... WARNING THIS LIBRARY IS NOT OPTIMIZED........................ #
#... AND MENT TO BE USED ON RELATIVELY SMALL VECTOR/SETS...........#
####################################################################

# these are mainly shortcuts
zipl = lambda *x : [list(_) for _ in zip(*x)]
mapl = lambda f,x : list(map(f,x))
avg = lambda x : sum(x)/len(x)
diff = lambda x : [x[i]-x[i-1] for i in range(1,len(x))]
ratio = lambda x : [x[i]/x[i-1] for i in range(1,len(x))]

slices = lambda seq,inp : [seq[i:i+inp] for i in range(len(seq)-(inp-1))]
sma = lambda seq,inp : mapl(avg,slices(seq,inp))
stoch = lambda seq,inp : mapl(lambda x : (max(x)-x[-1])/(max(x)-min(x)),slices(seq,inp))

# how to make an rsi:
positive = lambda x :  mapl(lambda x: x if x > 0 else 0 ,diff(x))
absolute = lambda x : mapl(abs,diff(x))
local_rsi = lambda x : sum(positive(x))/sum(absolute(x))
rsi = lambda seq,inp : mapl(local_rsi,slices(seq,inp))

# bollinger bands:
from math import sqrt
std_deviation = lambda x :sqrt((avg([(_-avg(x))**2 for _ in x])))
sd = lambda seq,inp : mapl(std_deviation, slices(seq,inp))
bb = lambda seq, inp : [(x+y,x,x-y) for x,y in zip(sma(seq,inp),sd(seq,inp))]

# ema
def emafy(x,k):
    memo = x[0]
    for _ in x:
        new = (memo*(k-1)+_)/k
        memo = new
        yield new

emafly = lambda x,k : list(emafy(x,k))
ema = lambda seq,inp : emafly(sma(seq,inp),inp)


