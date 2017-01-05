#encoding=utf-8
import csv

doc = [] 
query = [] 
reldict = []
entdict = []


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
	with open("relation.txt", "r") as relation :
	    for line in relation :
	    	line = line.replace("\n","")
	    	currentline = line.split(" ")
	    	reldict.append(currentline)
def inputentity() :
	with open("entity.txt", "r") as entity :
	    for line in entity :
	    	line = line.replace("\n","")
	    	currentline = line.split(" ")
	    	entdict.append(currentline)



inputdoc()
inputquery()
inputrelation()
inputentity()
