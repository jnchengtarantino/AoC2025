import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    arr = np.array([[int(x) for x in lines[i].strip().split()] for i in range(len(lines) - 1)])
    ops = lines[-1].strip().split()
    return sum([reduce(lambda x,y: x+y, arr[:,i]) if ops[i] == '+' else (reduce(lambda x,y: x*y, arr[:,i])) for i in range(arr.shape[1])])

def part2(lines):
    ops = lines[-1].strip().split()
    charArr = np.array([[c for c in line[:-1]] for line in lines[:-1]])
    nums = [''.join(charArr[:,i]).strip() for i in range(charArr.shape[1])]
    split = splitArr(nums)
    return sum([reduce(lambda x,y: x+y, split[i]) if ops[i] == '+' else (reduce(lambda x,y: x*y, split[i])) for i in range(len(split))])
    
def splitArr(inList: list[str]):
    res = []
    cur = []
    for e in inList:
        if e.strip() == '':
            res.append(cur)
            cur = []
        else:
            cur.append(int(e))

    res.append(cur)
    return res

if __name__ == "__main__":
    testFile = open("test.txt")
    testLines = testFile.readlines() 
    print(" --- TEST --- ")
    print(f'Part 1 : {part1(testLines)}')      
    print(f'Part 2 : {part2(testLines)}')
    testFile.close()

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(f'Part 1 : {part1(inLines)}')      
    print(f'Part 2 : {part2(inLines)}')
    inFile.close()