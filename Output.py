#encoding=utf-8
import csv

def output(rellist) :
	outputlist = []
	col  = ['Id', 'Property']  
	outputlist.append(col)
	outputlist += rellist
	output = open("vote.csv","w")
	w = csv.writer(output)
	w.writerows(outputlist)
	output.close()

