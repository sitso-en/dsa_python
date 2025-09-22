"""Question 8: Advanced Dictionary Manipulation 
Write a function group_by_category(items) that groups a list of dictionaries by a 
category key. 
Example: 
items = [ 
{"name": "apple", "category": "fruit"}, 
{"name": "carrot", "category": "vegetable"}, 
{"name": "banana", "category": "fruit"} 
] 
group_by_category(items) 
Returns: 
{ 
} 
"fruit": ["apple", "banana"], 
"vegetable": ["carrot"] """

def group_by_category(items):

    categorised = {} #dict in whice the data will be categorsied
    for item in items:
        #extract the values of these keys into variables
        category =item["category"]
        name = item["name"]
        
        #create an empty list if category is no in the dictionary
        if category not in categorised:
            categorised[category] = []
            #add one after the other the names of the items according to their categories
        categorised[category].append(name)
    print (categorised)

def main():
    items = [ 
    {"name": "apple", "category": "fruit"}, 
    {"name": "carrot", "category": "vegetable"}, 
    {"name": "banana", "category": "fruit"} 
    ]

    group_by_category(items)

if __name__ == "__main__":
    main()   