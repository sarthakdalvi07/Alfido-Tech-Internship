# Task 2: API Integration & JSON Handling
# Author: Sarthak Dalvi

import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    response.raise_for_status()

    users = response.json()

    print("Users from API:\n")

    for user in users:
        print(f"Name : {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City : {user['address']['city']}")
        print("-" * 30)

    
    search = input("\nEnter name to search: ")

    found = False
    for user in users:
        if search.lower() in user["name"].lower():
            print("\nUser Found")
            print(user)
            found = True

    if not found:
        print("User not found.")

except requests.exceptions.RequestException as e:
    print("API Error:", e)