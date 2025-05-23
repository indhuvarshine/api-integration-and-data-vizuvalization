import requests
import json
import matplotlib.pyplot as plt

# GitHub API endpoint
url = "https://api.github.com/users/octocat"

# Send GET request
response = requests.get(url)

# Check if response was successful
if response.status_code == 200:
    # Parse JSON response
    user_data = response.json()
    print("User Data:")
    print(json.dumps(user_data, indent=4))
else:
    print("Failed to retrieve data")
