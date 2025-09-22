"""Question 1: String Manipulation 
Write a function capitalize_words(sentence) that takes a string and capitalizes the first 
letter of each word. 
 Example: 
 capitalize_words("hello world from python") # "Hello World From Python"""

def capitalise_words(string):
    return string.title() #title capitalizes each word in a string

def main():
    print(capitalise_words(input("Enter a string: ")))
    
if __name__ == "__main__":
    main()