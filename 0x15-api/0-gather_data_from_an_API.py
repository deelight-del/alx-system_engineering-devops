#!/usr/bin/python3
""" This file accesses a REST API
and prints out some information based on the passed id
as an integer"""


if __name__ == "__main__":
    import requests
    import sys

    emp_id = int(sys.argv[1])
    if isinstance(emp_id, int):
        users_url = 'https://jsonplaceholder.typicode.com/users'
        todos_url = 'https://jsonplaceholder.typicode.com/todos'
        users_list_json = requests.get(users_url)
        users_list = users_list_json.json()
        for user in users_list:
            if user.get('id') == emp_id:
                emp_name = user.get('name')
                todos_list_json = requests.get(todos_url)
                todos_list = todos_list_json.json()
                todo_title_completed = {
                    todo.get('title'): todo.get('completed') for todo in
                    todos_list if todo.get('userId') == emp_id
                }
                total = len(todo_title_completed)
                done = sum(todo_title_completed.values())
                print(
                    f"Employee {emp_name} is done with tasks({done}/{total}):"
                )
                for title, completed in todo_title_completed.items():
                    if completed:
                        print(f"\t {title}")
                break
