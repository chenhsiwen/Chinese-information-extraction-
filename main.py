#encoding=utf-8
import Input 
import Output 
import random


query = Input.query
doc = Input.doc 
reldict = Input.reldict 
output = Output.output


rellist = []
tokenlist = []

def markentity(query,doc):
	tokenlist = []
	tokenquery = []
	tokenqueries = []
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


def markrelation (tokenlist, reldict):
	tokenquery = [] 
	for i in range (len(tokenlist)) :
		for j in range (len(tokenlist[i])) :
			did = tokenlist[i][j][0]
			for k in range (len(reldict)) :
				for l in range (1,len(reldict[k])) :
					location = doc[did].find(reldict[k][l])
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
			entity = []
			relation = [] 
			for k in range (1,len(tokenlist[i][j])) :
 				if type(tokenlist[i][j][k][0])  == str :
 					entity.append(tokenlist[i][j][k])
 				else :
 					relation.append(tokenlist[i][j][k])
			for k in range (len(entity)) :
 				for l in range (len(relation)) :
 			 		vote[relation[l][0]] += tokenlength(entity[k],relation[l])		
		maxval = max(vote)
		if maxval != 0 :
			rid = vote.index(maxval)
		else :
			rid = random.randint(0,6)
		rellist.append([query[i+1][0],reldict[rid][0]])
	return rellist


def tokenlength (entity, relation):
	delta = abs(entity[1] - relation[1])
	if delta == 0 :
		return 0 
	else : 
		return 1 / delta






tokenlist = markentity(query, doc)
tokenlist = markrelation(tokenlist, reldict)

rellist = voterelation(tokenlist)

output(rellist)