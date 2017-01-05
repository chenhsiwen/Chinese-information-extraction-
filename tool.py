#encoding=utf-8

def lev(str1, str2):
	if not str1: return len(str1)
	if not str2: return len(str2)
	return min(lev(str1[1:], str2[1:])+(str1[0] != str2[0]), lev(str1[1:], str2)+1, lev(str1, str2[1:])+1)
def sim(str1, str2) :
	return 1 - lev(str1,str2)/max(len(str1),len(str2))

