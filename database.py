import json

def save_tasks_to_file(task_list, file_path="tasks.json"):
    tasks = [task_list.item(i).text() for i in range(task_list.count())]
    with open(file_path, "w") as file:
        json.dump(tasks, file)

def load_tasks_from_file(task_list, file_path="tasks.json"):
    try:
        with open(file_path, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_list.addItem(task)
    except FileNotFoundError:
        pass
