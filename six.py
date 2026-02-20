"""Question 6: Sorting & Finding 
Write a function second_largest(lst) that finds the second largest number in a list without 
using sorted()."""

def second_largest(lst):
    largest = 0
    for num in lst:
        if num > largest:
            largest = num
    return largest

def main():
    numbers = [5, 2, 6, 2,1, 8, 7, 1, 4,3]
    print(second_largest(numbers))
