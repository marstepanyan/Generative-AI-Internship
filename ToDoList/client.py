import requests

url = 'http://localhost:5000'


def get_task_by_id(task_id):
    response = requests.get(f'{url}/todos/{task_id}')
    return response.json()


def get_tasks():
    response = requests.get(f'{url}/todos')
    return response.json()


def create_task(title, description):
    data = {"title": title, "description": description}
    response = requests.post(f'{url}/todos', json=data)
    return response.json()


def update_task(task_id, title=None, description=None):
    data = {}
    if title:
        data["title"] = title
    if description:
        data["description"] = description
    response = requests.patch(f'{url}/todos/{task_id}', json=data)
    return response.json()


def delete_task(task_id):
    response = requests.delete(f'{url}/todos/{task_id}')
    return response.json()


if __name__ == '__main__':
    task_by_id_1 = get_task_by_id(1)
    print("Task By ID 1:", task_by_id_1)

    task = create_task("New Task", "Sleep")
    print("Created Task:", task)

    updated_task = update_task(task["id"], title="Sleeping")
    print("Updated Task:", updated_task)

    task_list = get_tasks()
    print("Task List:", task_list)

    deleted_task = delete_task(updated_task["id"])
    print("Deleted Task:", deleted_task)

    task_list_after = get_tasks()
    print("Task List After:", task_list_after)
