""" Question 4: List of Dictionaries 
You have a list of products: 

Write a function get_affordable_products(products, budget) that returns all products 
with a price less than or equal to budget."""


def get_affordable_products(products, budget):
    found = False
    for product in products:
        if product["price"] <= budget:
            print(f"Name: {product['name']}, Price: {product['price']}")
            found = True
    if not found:
        print("There is no product in your budget here!")

def main():
    products = [ 
        {"name": "Laptop", "price": 1200}, 
        {"name": "Phone", "price": 800},
        {"name": "Tablet", "price": 600}
    ]

    budget = int(input("Enter your budget: "))
    get_affordable_products(products, budget)

if __name__ == "__main__":
    main()
