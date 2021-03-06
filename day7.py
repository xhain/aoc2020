#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:08:52 2020

@author: max
"""


# Advent of Code 2020
# Day 7, part 1 & 2
# https://adventofcode.com/2020/day/7

data = [line.rstrip() for line in list(open("data/input7.txt", "r"))]

test1, test_ans1 = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags."
        ], 4

test2, test_ans2 = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags."
    ], 126


# Part 1 Solution
def get_bags(color, rules):
    # All lines that contain our target color, if not in first position of string (inner)
    lines = [line for line in rules if color in line and line.index(color) != 0]
    colorsTracker = []
    
    if len(lines) == 0:
        return []
    
    else: 
        colors = set([line[:line.index(" bags")] for line in lines])
        
        for color in colors:
            colorsTracker.append(color)
            bags = get_bags(color, rules)
            colorsTracker += bags
     
    return set(colorsTracker)
    

# Part 2 Solution
def get_count(color, rules):
    # All lines that do contain our target color in the first position (outer)
    rule = ''.join(line for line in rules if line[:line.index(' bags')] == color)
    
    # Terminate if rule contains "no other bags"
    if 'no other bags' in rule:
        return 1
    
    # Retrieve all types + amount as sliced list (count + adjective + color)
    rule = rule[rule.index('contain ')+len('contain '):].split()
    ans, i = 0, 0
    
    # Iterate over sliced list, retrieve amount of bags and color of bag
    while i < len(rule):
        amount = int(rule[i])
        color = rule[i+1] +' '+ rule[i+2]
        ans += amount * get_count(color, rules)
        i += 4
    return ans + 1


# Results
assert len(get_bags('shiny gold', test1)) == test_ans1
assert get_count('shiny gold', test2)-1 == test_ans2
print("/ part 1: ", len(get_bags('shiny gold', data)))
print("/ part 2: ", get_count('shiny gold', data)-1)

# That took too long. I need to practice recursions.
