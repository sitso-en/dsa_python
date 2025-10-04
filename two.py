"""Question 2: List Methods 
Given a list of numbers, do the following using list comprehensions and built-in functions: 
● Double each number 
 
● Keep only even numbers 
 
● Find the sum of the remaining numbers

Example: 
process_list([1,2,3,4,5]) # 12  """

#per my understanding

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#double each number
doubled = [x * 2 for x in numbers]
print(f"Doubled numbers: {doubled}")

#keep even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

#keep rest of numbers that are not even and sum them
total = sum(x for x in numbers if x % 2 != 0)
print(f"Sum of the remaining (odd) numbers: {total}")