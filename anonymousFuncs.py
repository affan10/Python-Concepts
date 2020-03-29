'''
    This script is an implementation of Lamda Functions with map(), filter() and reduce()
    Anonymous Functions = Lambda Expressions = Lambda Function(s)
'''

# Simple Lambda Expression to calculate corresponding y coordinate given x, m and c
# Either return the Lambda Expression into a variable and pass values to that as follows:
equation = lambda x, m, c: m * x + c
print('With variable:', equation(1, -2, 10))

# Or pass values directly to the Lambda Expression like this:
print('Without variable:', (lambda x, m, c: m * x + c)(1, -2, 10))

'''
    Using map() with Lambda Expressions
    map() performs the given function to all values in the passed iterable
'''
# Convert lowercase strings in list to uppercase
lowerStrings   = ['messi', 'iniesta', 'xavi', 'puyol', 'pique']
convertToUpper = lambda name : name.upper()
print(list(map(convertToUpper, lowerStrings)))

'''
    Using filter() with Lambda Expressions
    filter() returns values depending on the filter critera defined in the lambda function
'''
# Remove missing values from list
lowerStrings        = ['messi', '', 'iniesta', '', '', 'xavi', 'puyol', 'pique', '', '']
removeMissingValues = lambda name : name
print(list(filter(removeMissingValues, lowerStrings)))

'''
    Using reduce() with Lambda Expressions
    reduce() always requires at least two values in its lamdba function
    It performs the operation specified in the lambda function and computes the result of 
    the first two values. It then uses the result to perform the operation on the next value
'''
from functools import reduce
# Concatenate all strings in the list
lowerStrings   = ['messi', 'iniesta', 'xavi', 'puyol', 'pique']
concateStrings = lambda x, y : x + y
print(reduce(concateStrings, lowerStrings))
