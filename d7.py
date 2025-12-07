import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache, lru_cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    start, levels = parseInput(lines)
    beams = [{start}]
    splits = 0
    for i, level in enumerate(levels):
        newBeams = set()
        for x in beams[i]:
            if x in level:
                newBeams.add(x-1)
                newBeams.add(x+1)
                splits += 1
            else:
                newBeams.add(x)
        beams.append(newBeams)
        # print(''.join(['^' if j in level else '.' for j in range(20)]))
        # print(''.join(['|' if j in newBeams else '.' for j in range(20)]))
    # print(levels)
    # print(beams)
    return splits

def part2(lines):
    start, levels = parseInput(lines)

    @lru_cache
    def traverse(depth, x):
        if depth == len(levels): 
            return 1
        elif x in levels[depth]:
            return traverse(depth+1, x-1) + traverse(depth+1, x+1)
        else:
            return traverse(depth+1, x)
    
    return traverse(0, start)

def parseInput(lines: list[str]):
    start = 0
    levels = []
    for line in lines:
        if 'S' in line:
            start = line.find('S')
        if '^' in line:
            levels.append({i for i,x in enumerate(line) if x == '^'})
    return start, levels

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