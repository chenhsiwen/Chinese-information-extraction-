#encoding=utf-8
import csv

doc = [] 
query = [] 
relation = []



def inputdoc() :
	with open("ref_text.txt", "r") as ref_text :
	    for line in ref_text :
	    	line = line.replace("\n","")
	    	line = line.replace("。","")
	    	doc.append(line)

def inputquery() :
	with open('test.csv', 'r') as test :
		spamreader = csv.reader(test)
		for row in spamreader:
			query.append(row)


def inputrelation() :
	with open("relation.txt", "r") as reldict :
	    for line in reldict :
	    	line = line.replace("\n","")
	    	currentline = line.split(" ")
	    	relation.append(currentline)


inputdoc()
inputquery()
inputrelation()
