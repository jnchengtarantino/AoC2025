import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    ranges, fruits = parseInput(lines)
    return sum([1 if any([lower <= fruit <= upper for lower, upper in ranges]) else 0 for fruit in fruits])

def part2(lines):
    ranges, _ = parseInput(lines)
    mergedRanges = set()

    for currLower, currUpper in ranges:
        toBeRemoved = set()

        for testLower, testUpper in mergedRanges:            
            if (currLower <= testLower <= currUpper) or (testLower <= currLower <= testUpper):
                currLower = min(currLower, testLower)
                currUpper = max(currUpper, testUpper)
                toBeRemoved.add((testLower, testUpper))
        
        mergedRanges = mergedRanges - toBeRemoved
        mergedRanges.add((currLower, currUpper))
    
    return sum([1+upper-lower for lower, upper in mergedRanges])


    
def parseInput(lines: list[str]):
    ranges = set()
    fruits = set()

    for line in lines:
        if line.strip() == '': pass
        elif '-' in line:
            l, u = line.strip().split('-')
            ranges.add((int(l), int(u)))
        else:
            fruits.add(int(line.strip()))
    
    return ranges, fruits

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