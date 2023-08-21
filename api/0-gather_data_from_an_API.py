#!/usr/bin/python3
"""Script that, using this REST API, for a given employee"""
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # Récupérer l'ID de l'employé depuis les arguments de ligne de commande
    employee_id = argv[1]

    # Obtenir les informations sur l'utilisateur depuis l'API
    user_data = requests.get(f"{API_URL}/users/{employee_id}").json()

    # Obtenir la liste des tâches à faire pour l'employé depuis l'API
    todo_data = requests.get(f"{API_URL}/todos?userId={employee_id}").json()

    # Filtrer les tâches terminées
    completed_tasks = [task['title'] for task in todo_data if task['completed']]

    # Nom de l'employé, nombre de tâches terminées et nombre total de tâches
    employee_name = user_data["name"]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Afficher les informations
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")
