
def return_Label(line):
    line = line.split(",")
    return line[0]



def countWord(line):
    line = line.rstrip()
    lines = MeCab.parse(line)
    words = lines.sprit(" ")
    for word in words:
        w2f[word] = w2f[label].get(word,0) + 1
    return w2f

import sys
import MeCab

args = sys.argv

w2f = {}
L2f = {}
L2w2f = {}
mailcount = 0
with open(args[1], 'r') as fp:
    for line in fp:
        label = return_Label(line)
        L2f[label] = L2f.get(label,0) + 1
        L2w2f[label] = L2w2f.get(label,{})
        mailcount += 1
        w2f = countWord(line)
        for word in L2w2f:
            L2w2f[label][word] = L2w2f[label].get(word,0) + w2f[word]
print(L2w2f)
