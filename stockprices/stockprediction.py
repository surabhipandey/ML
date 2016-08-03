import statistics as st
import math
testdict = {}
def printTransactions(m, k, d, name, owned, prices):
    #print ""
    traindict = {'CAL': 124.33, 'UCB': 63.46, 'RIT': 285.38,'UCLA':17.56,\
            'UCSC':334.312,'UFL':57.16,'UMAD':125.76,'RICE':124.12,'UMD':80.06,'USC':194.25}
    nooftrans = 0
    selldict = {}
    buydict = {}
    for i in range(k):
	samplemean = st.mean(prices[i])
    	testdict[name[i]] = traindict[name[i]]-samplemean
    s = sorted(testdict.items(), key=lambda x: x[1])
    p = dict(s)
    for key in p:
	i = name.index(key)
	#print key,p[key],prices[i][4]	
        if p[key] > 0 and prices[i][4] <= m:
	    	nooftrans = nooftrans+1
                cal = int(math.floor(m/prices[i][4]))
		m = m - cal*prices[i][4]
                buydict[key] = cal
        elif p[key] <= 0 and owned[i] > 0:
                nooftrans = nooftrans+1
		selldict[key] = owned[i]
    print nooftrans
    for key in buydict:
	print key+ ' BUY '+str(buydict[key])
    for key in selldict:
	print key+ ' SELL '+str(selldict[key])	
if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)


