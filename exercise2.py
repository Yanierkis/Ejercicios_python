"""
Exercise 2:

Consider the Fibonacci sequence.
It is a sequence of natural numbers defined recursively as follows:
the first element of the sequence is 0
the second element of the sequence is 1
each next element of the sequence is the sum of the previous two elements

The beginning of the Fibonacci sequence:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 

Find the sum of all even elements of the Fibonacci 
sequence with values less than 1,000,000 (1 million).

Present the solution in the form of a function called calculate().
In response, call calculate() function and print the result to the console.

Expected result:
1089154
"""

def calculate(num):
    #primero hacemos la sucesión de Fibonacci
    fib = [0,1]
    suma = 0
    
    while (fib[-1] < num):
        fib.append(fib[-1]+fib[-2])
        if (fib[-1]%2==0):
            suma = suma + fib[-1]
    
    return suma
    
print(calculate(1000000))
        
