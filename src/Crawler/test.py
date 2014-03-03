'''
Created on 26/02/2014

@author: chengyu
'''

import Parser
import re
from stemming.porter2 import stem
# from stemming.porter2 import stem
# a = stem("factionally")
# 
# print a

'''test re functions:'''

test_str = "\u0643\u0645 \u0644\u064a \u0648\u0627\u0646\u0627 \u0627\u0637\u0644\u0628 \u062d\u0633\u064a\u0646 \u0627\u0644\u062c\u0633\u0645\u064a \u064a\u0633\u0648\u064a \u0644\u064a \u0631\u062a\u0648\u064a\u062a \u0639\u0627\u062f \u0634\u0643\u0644\u0647 \u062d\u0646\u064a\u0651\u0646"


ma = Parser.MatrixParserForLearning()
  
k = ma.preExtractWords(test_str)
  
print k

print test_str.find(r'\\u[\w]{4}')


test_str2 = " Hahaha, pompommu lhoo mesti dtg pas aku gini :D RT@sagitaenggar: Hahaha lak yo malu seh aku X.X "

a = ma.prepocessString(test_str2)
print a

print "RT @zaynmalik: Meet my friend ... Jack Daniels :) he's cool, ha".startswith("RT")

print stem("I'm")

import pickle

a = {
  'a': 1,
  'b': 2
}

with open('file.txt', 'wb') as handle:
    pickle.dump(a, handle)

with open('file.txt', 'rb') as handle:
    b = pickle.loads(handle.read())

print a == b # True

