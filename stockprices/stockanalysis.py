import pandas as pd
from matplotlib import pyplot as plt
import statistics as st
import numpy as np
def dataanalysisstocks(price):
	print price
def plotstocks(y,label):
	#print y,label
	time = [x+1 for x in range(len(y))]
        plt.plot(time,y)
	plt.title(label+' mean '+str(st.mean(y))+ ' meadian '\
+str(st.median(y))+ ' stdev '+str(st.stdev(y)))
	#plt.ylabel('price')
	#plt.xlabel('time')
	print label,st.mean(y),np.percentile(y,30)
	#plt.show()
def readfile():
	with open('data') as f:
		for line in f:
			linelist = line.split()
			stock_name = linelist[0]
			stock_prices = linelist[1:]
			stck_prc = [float(x) for x in stock_prices]
			#print stock_name,stck_prc
			plotstocks(stck_prc,stock_name)
if __name__ == "__main__":
	readfile()
