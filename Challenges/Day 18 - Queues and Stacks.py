# https://www.hackerrank.com/challenges/30-queues-stacks/problem
# https://www.youtube.com/watch?v=wIFzL7E_YSA&list=PLGA4QH0Mda49NOaahSvnR_YpIRhjn_0m0&index=20


import sys
from collections import deque 
 
class Solution:
    # Write your code here
    def __init__(self):
        self.stack = list()
        self.queue = deque()
        
    def pushCharacter(self, Character):
        self.stack.append(Character)
    def enqueueCharacter(self, Character):
        self.queue.append(Character)
    
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.popleft()
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    