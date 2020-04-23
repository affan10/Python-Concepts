'''
    For List Comprehension
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get square of all numbers
result = [n * n for n in nums]
print(result)

# Get only those numbers that are even
result = [n for n in nums if n % 2 == 0]
print(result)

# Get (letter, number) for each number in '0123' and 'abcd'
result = [(letter, number) for letter in 'abcd' for number in range(4)]
print(result)

'''
    For Dictionary Comprehension
'''
# Create a dictionary with corresponding names and surnames
names     = ['Lionel', 'Andres', 'Xavi', 'Carles', 'Gerard']
surnames  = ['Messi', 'Iniesta', 'Hernandez', 'Puyol', 'Pique']
zipResult = list(zip(names, surnames))
print(zipResult)

fullNames = {name:surname for name, surname in zip(names, surnames)}
print(fullNames)

# Create a dictionary without Pique
fullNames = {name:surname for name, surname in zip(names, surnames) if surname != 'Pique'}
print(fullNames)

'''
    For Set Comprehensions
'''
# Add numbers to Set
nums   = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 13]
datSet = {n for n in nums}
print(datSet)

# Add only even numbers to Set
datSet = {n for n in nums if n % 2 == 0}
print(datSet)
