import math
def printTransactions(m, k, d, name, owned, prices):
    lines=[]
    buyDict = {}
    for index in range(k):
        if owned[index] > 0:
            if prices[index][4]>prices[index][3]:
                lines.append(name[index]+' SELL '+str(owned[index]))
    for index in range(k):
        if prices[index][4] < prices[index][3]:
            per = (prices[index][3]-prices[index][4])/prices[index][4]
            if per > 0.04:
                buyDict[per]=index
    for perc in sorted(buyDict.iterkeys(),reverse=True):
        index = buyDict[perc]
        units = int(math.floor(m/prices[index][4]))
        m = m - units*prices[index][4]
        if units>0:
            lines.append(name[index]+' BUY '+str(units))
        else:
            break
    print len(lines)
    for line in lines:
        print line

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
