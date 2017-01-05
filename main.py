#encoding=utf-8
import Input 
import Output 
import random
import tool


sim = tool.sim
query = Input.query
doc = Input.doc 
reldict = Input.reldict 
output = Output.output
entdict = Input.entdict

rellist = []
tokenlist = []


def entitytype (query):

	for i in range(1, len(query)) :
		query[i].append('person')
		token = 0
		for j in range (len(entdict)):
			if token != 1 :
				for k in range (1,len(entdict[j])) :
					position = query[i][2].find(entdict[j][k]) 
					if position != -1 :
						token = 1
						query[i].append(entdict[j][0])
						break
			else :
				break 
		if token != 1 :
			query[i].append(entdict[random.randint(0,2)][0])
	return query


def markentity(query,doc):
	tokenlist = []
	tokenquery = []
	tokenqueries = []
	for i in range(1, len(query)) :
		for k in range (len(doc)) :
			for j in range(1, 3) : 
				position = doc[k].find(query[i][j])
				if position != -1 :
					if j == 1 :
						tokenquery.append([query[i][3] ,position])
					else :
						tokenquery.append([query[i][4] ,position])
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
	count = 0
	for i in range (len(tokenlist)) :
		if (len(tokenlist[i]) == 0)	:
			count += 1
		for j in range (len(tokenlist[i])) :
			did = tokenlist[i][j][0]
			for k in range (len(reldict)) :
				for l in range (1,len(reldict[k])) :
					position = doc[did].find(reldict[k][l])
					if position != -1 :
						tokenquery.append([k,position])
			if (len(tokenquery) > 0) :				
				tokenlist[i][j]+= tokenquery
				tokenquery = []
	print (count)
	return tokenlist

def vote (tokenlist):
	for i in range (len(tokenlist)) :
		vote = [0,0,0,0,0,0,0]
		print (i,query[i+1][1],query[i+1][2])
		if query[i+1][4] == 'Place' :
			vote[4] = 0.3
			vote[5] = 0.3
			vote[6] = 0.3
		elif query[i+1][4] == 'workPlace' :
			vote[6] = 1
		else :
			if len(query[i+1][1])+len(query[i+1][2]) < 20 :
				if sim(query[i+1][1],query[i+1][2]) > 0.1 :
					vote[1] = 0.3
					vote[2] = 0.3
					vote[3] = 0.3		
				else :
					vote[0] = 0.25
					vote[1] = 0.25
					vote[2] = 0.25
					vote[3] = 0.25
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
 					vote[relation[l][0]] += tokendelta(entity[k],relation[l],len(entity),)		
		maxval = max(vote)
		rid = vote.index(maxval)
		# if maxval > 0 :
		# 	rid = vote.index(maxval)
		# else :
		# 	if query[i+1][4] == 'Place' :
		# 		rid = random.randint(4,5)
		# 	elif query[i+1][4] == 'workPlace' :
		# 		rid = 6
		# 	else :
		# 		if len(query[i+1][1])+len(query[i+1][2]) < 10 :
		# 			if sim(query[i+1][1],query[i+1][2]) > 0.1 :
		# 				rid = random.randint(1,3)
		# 			else :
		# 				rid = random.randint(0,3)
		# 		else :
		# 			rid = random.randint(0,3)
		rellist.append([query[i+1][0],reldict[rid][0]])
	return rellist

def tokendelta (entity, relation, entitylength):
	delta =abs(entity[1] - relation[1])
	if (entitylength > 1) :
		delta *= 0.5
	if delta == 0 :
		return 0 
	else : 
		return 1 / delta
		
query = entitytype(query)
tokenlist = markentity(query, doc)
tokenlist = markrelation(tokenlist, reldict)
rellist = vote(tokenlist)

output(rellist)