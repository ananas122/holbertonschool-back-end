#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # Retrieve user ID from command line arguments
    USER_ID = argv[1]

    # Get user information from the API
    user_response = requests.get(f"{API_URL}/users/{USER_ID}").json()

    # Get the list of tasks for the user from the API
    todo_response = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    # Prepare data for export
    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_response['username']
            }
            for task in todo_response
        ]
    }

    # Write data to a JSON file
    with open(f"{USER_ID}.json", mode='w') as json_file:
        json.dump(data, json_file)

    print(f"Data has been exported to {USER_ID}.json")
