#!/usr/bin/python3
""" This file accesses a REST API
and prints out some information based on the passed id
as an integer"""


if __name__ == "__main__":
    import json
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
                list_of_tasks_info = []
                for title, completed in todo_title_completed.items():
                    dict_task_info = {
                            "task": title,
                            "completed": completed,
                            "username": emp_name
                            }
                    list_of_tasks_info.append(dict_task_info)
                user_id_info_dict = {f"{emp_id}": list_of_tasks_info}
                with open(f"{emp_id}.json", "w") as file:
                    json.dump(user_id_info_dict, file)
                break
