# https://www.hackerrank.com/challenges/30-interfaces/problem

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total = 0
        for x in range(1,n+1):
            if n % x == 0:
                total += x
        
        
        return total

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)