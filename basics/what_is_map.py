# What does .map() even do in Python?
# So, from what I understand, it applies a function over an iterable. Map returns a map object, so you have to wrap it with a list() or a tuple() for it to be printable.

# So, list(map(lambda x: x*2 , [1,2,3,4])) should return [2,4,6,8]


# Write a function to convert a list of temperatures in Celsius to Fahrenheit using map()

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda x: x*9/5 + 32, celsius))

print(f"Task 1: Temperatures in Fahrenheit: {fahrenheit}")


# Given a list of names ["alice", "BOB", "ChArLie"], write a one-liner using map() and str.capitalize to get a properly capitalized list.

names = ["alice", "BOB", "ChArLie"]
names_proper = list(map( lambda x : x.lower().capitalize() , names))
print(f"Task 2: {names_proper}")


# Use map() to compute the final price after tax for each item.
prices = [100, 200, 300]
tax_rates = [0.1, 0.2, 0.15]

taxes = list(map(lambda x, y: x * y, prices, tax_rates))
print(f"Task 3: {taxes}")