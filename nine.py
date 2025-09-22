"""Question 9: Default & Safe Access 
Write a function get_user_city(user) that safely returns a user’s city. If the city is missing, 
return "Unknown". 
Example: 
user1 = {"name": "John", "address": {"city": "Lagos"}} 
get_user_city(user1) # "Lagos" 
user2 = {"name": "Mary"} 
get_user_city(user2) # "Unknown" """


def get_user_city(user):
    if "address" in user and "city" in user["address"]: #check if the is an address in user and if city is in this address and print if true
        print(f"City: {user['address']['city']}")
    else:
        print("Unknown") #print unknown if false

def main():
    user1 = {"name": "John", "address": {"city": "Lagos"}}
    get_user_city(user1)

    user2 = {"name": "Mary"}
    get_user_city(user2)

if __name__ == "__main__":
    main()