# https://www.hackerrank.com/challenges/30-review-loop/problem 

# Enter your code here. Read input from STDIN. Print output to STDOUT

S = int(input()) 
 
for x in range(S):
    N = input() 
    print(N[::2],N[1::2])
    
