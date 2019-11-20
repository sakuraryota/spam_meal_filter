# coding: utf-8

import sys
import MeCab

textFleq = 0
text = sys.argv[1]
tagger = MeCab.Tagger("-Owakati")

with open(text,'r') as file:

  for line in file:
   words = tagger.parse(line).split(' ')
   textFleq += len(words)
  print(textFleq)

