# https://www.hackerrank.com/challenges/30-review-loop/problem 

# Enter your code here. Read input from STDIN. Print output to STDOUT

S = int(input()) 
N = input() 
T = input() 

print(N[::S],N[1::S])
print(T[::S],T[1::S])

