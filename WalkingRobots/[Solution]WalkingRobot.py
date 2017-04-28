#!/bin/python3

import sys

def howManyCollisions(s):
    collisionCount = 0
    for x in range(0,len(s)):
      if s[x:x+1] is 'r':
        if 'l' in s[x:] or 'd' in s[x:]:
          collisionCount = collisionCount+1
      if s[x:x+1] is 'l':
        if 'r' in s[:x] or 'd' in s[:x]:
          collisionCount = collisionCount+1
    return collisionCount

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # Returns the number of times moving robots collide.
    result = howManyCollisions(s)
    print(result)
