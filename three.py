"""Question 3: Dictionary Unpacking Equivalent 
You are given this dictionary: 
user = { 
    "id": 1, 
    "profile": { 
        "username": "mandem", 
        "email": "mandem@example.com" 
    }, 
    "settings": { 
        "theme": "dark", 
        "notifications": True 
} 
}
Write a function that extracts the username, email and theme and prints them"""

user = { 
    "id": 1, 
    "profile": { 
        "username": "mandem", 
        "email": "mandem@example.com" 
    }, 
    "settings": { 
        "theme": "dark", 
        "notifications": True 
    } 
}

def extract_info():
    #user dictionary mathods to access and extract the name and email and theme the user
    print(user["profile"]["username"])
    print(user["profile"]["email"])
    print(user["settings"]["theme"])

def main():
    extract_info()

if __name__ == "__main__":
    main()