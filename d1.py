import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    moves = parseInput(lines)
    count, pos = 0, 50

    for move in moves:
        pos += move 
        if pos % 100 == 0:
            count += 1
    
    return count

def part2(lines):
    moves = parseInput(lines)
    count, pos = 0, 50
    
    for move in moves:
        for _ in range(abs(move)):
            pos += 1 if move > 0 else -1
            if pos % 100 == 0:
                count += 1
    
    return count
    
def parseInput(lines: list[str]):
    return [-1 * int(line[1:]) if line[0] == 'L' else int(line[1:]) for line in lines]

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