""""
Question 5: *args and Set Union 
Write a function merge_lists(*lists) that accepts multiple lists and merges them into a 
single unique list (no duplicates). 
Example: 
merge_lists([1,2], [2,3], [3,4]) # [1,2,3,4] """

def merge_lists(a, b, c):
    return(list(set(a+b+c))) #add them as a set to allow for no duplicates print as a list

def main():
    a = [1, 2]
    b = [2, 3]
    c = [3, 4]
    print (merge_lists(a, b, c))

if __name__ == "__main__":
    main()
