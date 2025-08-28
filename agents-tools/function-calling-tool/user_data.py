import requests
from agents import function_tool 


@function_tool
def fetch_user_data():
    """Fetch user data from a public API."""
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    print("Fetch user data function called")
    return res.json()


@function_tool
def fetch_user_data_by_id(id: int):
    """Fetch user data from a public API."""
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    res = requests.get(url)
    print("Fetch user data by id function called")
    return res.json()
    

  