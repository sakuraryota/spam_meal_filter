def return_Label(line): 
	Line = line.split(",") 
	return Line[0] 

def countWord(Line,line,L2w2f):
	lines = line.rstrip()
	line_word = mecab.parse(lines)
	words = line_word.sprit(" ")
	for word in words:
		L2w2f[line][word] = L2w2f[L].get(word,0) + 1
	return L2w2f

import sys 
import MeCab 
 
args = sys.argv 

L2f={}  
L2w2f={}  
mailcount=0 
with open(args[1],'r') as fp: 
	for line in fp: 
		Line = return_Label(Line) 
		L2f[Line] = L2f.get(Line,0) +1 
		L2w2f[line] = L2W2f.get(Line,{})
		mailLen +=1
