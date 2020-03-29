'''
    This script compares execution time of Generators to list comprehensions
    and iteration via for loops.
'''

import timeit
import functools

# Create list of numbers up to 10 million numbers
nums = [n for n in range(1, 10000001)]

'''
    Without using Generator; with simple for loop
'''

def squaresForLoop(nums):
    result = []
    for n in nums:
        result.append(n * n)
    
    return result

print('Time elapsed with for loop:', timeit.timeit(functools.partial(squaresForLoop, nums), number=1), 'seconds')

'''
    Without using Generator; with list comprehension
'''
def squaresListComprehension(nums):
    return [n * n for n in nums]

print('Time elapsed with list comprehension:', timeit.timeit(functools.partial(squaresListComprehension, nums), number=1), 'seconds')

'''
    By using Generator Expression
'''
def squaresGeneratorExpression(nums):
    return (n * n for n in nums)

print('Time elapsed with Generator Expression:', timeit.timeit(functools.partial(squaresGeneratorExpression, nums), number=1), 'seconds')

def squaresGenerator(nums):
    for n in nums:
        yield n * n

print('Time elapsed with Generator:', timeit.timeit(functools.partial(squaresGeneratorExpression, nums), number=1), 'seconds')