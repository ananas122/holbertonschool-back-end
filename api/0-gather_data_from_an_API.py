#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""
import requests
from sys import argv


if __name__ == '__main__':
    URL = 'https://jsonplaceholder.typicode.com'

    # Récupérer l'ID de l'employé depuis les arguments de ligne de commande
    employee_id = argv[1]

    # Obtenir les infos sur l'user
    user_data = requests.get(f"{API_URL}/users/{employee_id}").json()

    # Obtenir la liste des tâches à faire pour l'employé
    todo_data = requests.get(f"{API_URL}/todos?userId={employee_id}").json()

    # Filtrer les tâches terminées
    completed_task_titles = [task['title'] for task in todo_data if task['completed']]

    # Calculer le nombre total de tâches
    total_tasks = len(todo_data)

    # Afficher le résultat
    print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in sum_tasks:
        print(f"    {task}")

