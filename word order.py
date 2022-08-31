# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

nbWords = int(input())
nbDistinct = 0
ordered = OrderedDict()
s = ""

for v in range(nbWords):
    w = input()
    if w in ordered:
        ordered[w] += 1
    else: 
        ordered[w] = 1
        nbDistinct += 1
    
print(nbDistinct)
for i, v in enumerate(ordered.items()):
    s = s + (" " if i > 0 else "") + str(v[1])
print(s)
