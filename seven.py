"""Question 7: Higher Order Functions 
Write a function apply_operation(lst, operation) where operation can be "square", 
"double", or "negate", and apply it to every element of the list. 
Example: 
apply_operation([1,2,3], "square") # [1,4,9] """

def apply_operation(lst, operation):
    if operation == "square":
        return [x**2 for x in lst] #list comprehension for squaring a number
    elif operation == "negate":
        return[-x for x in lst] #list comprehension for negation.
    elif operation == "double":
        return[x*2 for x in lst] #list comprehension for doubling

def main():
    #take in numbers into a list, making them ints using the map function
    lst = list(map(int, input("List of numbers: ").split())) #every number is divided by a split
    operation = input("Operations(Square, Double, Negate): ").lower() #change the user input to lower case
    print(apply_operation(lst, operation))

if __name__ == "__main__":
    main()