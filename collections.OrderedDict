# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

nbItems = int(input())
orderedDict = OrderedDict()

for i in range(nbItems):
    p = ""
    inp = input().split()
    tmp = []
    for v in enumerate(inp):
        if (isinstance(v[1], str) and not v[1].isdigit()):
            # p += v[1]
            tmp.append(v[1])
        else: price = int(v[1])
    p = " ".join(tmp)
    if (p in orderedDict):
        orderedDict[p] += price
    else : orderedDict[p] = price

for v in orderedDict.items():
    print(v[0] + " " + str(v[1]))
