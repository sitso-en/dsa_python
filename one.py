"""String Manipulation 
Write a function capitalize_words(sentence) that takes a string and capitalizes the first 
letter of each word. 
 """

def capitalise_words(string):
    return string.title() #title capitalizes each word in a string

def main():
    print(capitalise_words(input("Enter a string: ")))
    
if __name__ == "__main__":
    main()
