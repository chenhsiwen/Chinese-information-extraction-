#encoding=utf-8
import Input 
import Output 
import random


query = Input.query
doc = Input.doc 
relation = Input.relation 
output = Output.output

rellist = []
tokenlist = []

def markentity(query,doc):
	tokenlist = []
	tokenqueries = []
	tokenquery = [] 
	for i in range(1, len(query)) :
		for k in range (len(doc)) :
			for j in range(1, 3) : 
				location = doc[k].find(query[i][j])
				if location != -1 :
					if j == 1 :
						tokenquery.append(['f'  ,location])
					else :
						tokenquery.append(['s'  ,location])
			if (len(tokenquery) > 0) :
				temp = [k]
				temp +=  tokenquery
				tokenqueries.append(temp)
			tokenquery = []
		tokenlist.append(tokenqueries)
		tokenqueries = []
	return tokenlist


def markrelation (tokenlist, relation):
	tokenquery = [] 
	for i in range (len(tokenlist)) :
		for j in range (len(tokenlist[i])) :
			did = tokenlist[i][j][0]
			for k in range (len(relation)) :
				for l in range (1,len(relation[k])) :
					location = doc[did].find(relation[k][l])
					if location != -1 :
						tokenquery.append([k,location])
			if (len(tokenquery) > 0) :				
				tokenlist[i][j]+= tokenquery
				tokenquery = []
	return tokenlist

def voterelation (tokenlist):
	for i in range (len(tokenlist)) :
		vote = [0,0,0,0,0,0,0]
		for j in range (len(tokenlist[i])) :
	 		for k in range (1,len(tokenlist[i][j])) :
	 			for l in range (len(tokenlist[i][j][k])) :
	 				for m in range (len(relation)):
	 					if tokenlist[i][j][k][0] == m :
	 						vote[m] += 1;
		maxval = max(vote)
		if maxval != 0 :
			rid = vote.index(maxval)
		else :
			rid = random.randint(0,6)
		rellist.append([query[i+1][0],relation[rid][0]])
	return rellist




tokenlist = markentity(query, doc)

tokenlist = markrelation(tokenlist, relation)

print (tokenlist)
rellist = voterelation(tokenlist)

for i in range (len(rellist)) :
	print (rellist[i]) 

output(rellist)