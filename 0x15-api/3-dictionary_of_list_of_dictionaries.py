#!/usr/bin/python3
""" This file accesses a REST API
and prints out some information based on the passed id
as an integer"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    emp_list = requests.get(users_url).json()
    todo_all_dict = dict()
    for emp in emp_list:
        emp_id = emp.get('id')
        each_id_list = []
        todos_list = requests.get(todos_url).json()
        for todo in todos_list:
            if todo.get('userId') == emp.get('id'):
                each_id_list.append(
                        {
                            'username': emp.get('username'),
                            'task': todo.get('title'),
                            'completed': todo.get('completed')
                            }
                        )
        emp_id_dict = {emp.get('id'): each_id_list}
        todo_all_dict.update(emp_id_dict)
    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(todo_all_dict, outfile)
