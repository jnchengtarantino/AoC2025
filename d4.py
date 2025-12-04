import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    map = parseInput(lines)
    res = 0

    for y in range(1, len(map) - 1):
        for x in (range(1, len(map[y])-1)):
            if map[y][x] == '@':
                if sum(map[y+j][x+i] == '@' for i in (-1,0,1) for j in (-1,0,1)) < 5: res +=1

    return res

def part2(lines):
    map = parseInput(lines)
    removed = set()
    prevSize = -1

    while prevSize != len(removed):
        prevSize = len(removed)
        toBeRemoved = set()

        for y in range(1, len(map) - 1):
            for x in (range(1, len(map[y])-1)):

                if map[y][x] == '@' and (y,x) not in removed:
                    
                    aroundSum = 0
                    for j in (-1,0,1):
                         for i in (-1,0,1):
                            if map[y+j][x+i] == '@' and (y+j,x+i) not in removed: aroundSum +=1
                    
                    if aroundSum < 5:
                        toBeRemoved.add((y,x))

        removed.update(toBeRemoved)

    
    return(len(removed))
    
def parseInput(lines: list[str]):
    m = ['.' + line.strip() + '.' for line in lines]
    m.insert(0, '.' * (len(lines[0].strip()) + 2))
    m.append('.' * (len(lines[0].strip()) + 2))
    return m

if __name__ == "__main__":
    # testFile = open("test.txt")
    # testLines = testFile.readlines() 
    # print(" --- TEST --- ")
    # print(f'Part 1 : {part1(testLines)}')      
    # print(f'Part 2 : {part2(testLines)}')
    # testFile.close()

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(f'Part 1 : {part1(inLines)}')      
    print(f'Part 2 : {part2(inLines)}')
    inFile.close()