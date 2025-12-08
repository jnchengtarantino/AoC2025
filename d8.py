import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm, prod
import re

def part1(lines,nMin):
    boxes = parseInput(lines)
    boxDistance = [(i, j, distSq(boxes[i],boxes[j])) for i in range(len(boxes)) for j in range(i + 1, len(boxes))]
    sortedBoxInd = sorted(boxDistance, key = lambda x: x[2])[:nMin]

    disjSet = DisjSet(len(boxes))
    for i, j, _ in sortedBoxInd: 
        disjSet.join(i,j)
    count = disjSet.getCounter()
    return prod([c for _, c in count.most_common(3)])


def part2(lines):
    boxes = parseInput(lines)
    boxDistance = [(i, j, distSq(boxes[i],boxes[j])) for i in range(len(boxes)) for j in range(i + 1, len(boxes))]
    sortedBoxInd = sorted(boxDistance, key = lambda x: x[2])

    disjSet = DisjSet(len(boxes))
    for i, boxInd in enumerate(sortedBoxInd):
        disjSet.join(boxInd[0], boxInd[1])
        if disjSet.isWhole():
            return boxes[boxInd[0]][0] * boxes[boxInd[1]][0]

def parseInput(lines: list[str]):
    return [tuple([int(i) for i in line.strip().split(',')]) for line in lines]

def distSq(a: tuple[int,int,int], b: tuple[int,int,int]):
    return sum([ (a[i]-b[i]) ** 2 for i in range(3)])

class DisjSet:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] == i: return i
        else: 
            rep = self.find(self.parent[i])
            self.parent[i] == rep
            return rep
    
    def join(self, i, j):
        iRep = self.find(i)
        jRep = self.find(j)
        self.parent[iRep] = jRep

    def getCounter(self):
        return Counter([self.find(i) for i in range(len(self.parent))])
    
    def isWhole(self):
        return len(set([self.find(i) for i in range(len(self.parent))])) == 1

if __name__ == "__main__":
    testFile = open("test.txt")
    testLines = testFile.readlines() 
    print(" --- TEST --- ")
    print(f'Part 1 : {part1(testLines,10)}')      
    print(f'Part 2 : {part2(testLines)}')
    testFile.close()

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(f'Part 1 : {part1(inLines,1000)}')      
    print(f'Part 2 : {part2(inLines)}')
    inFile.close()