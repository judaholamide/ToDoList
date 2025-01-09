def add_task(task_list, task):
    if task:
        task_list.addItem(task)

def delete_task(task_list):
    selected_item = task_list.currentItem()
    if selected_item:
        task_list.takeItem(task_list.row(selected_item))
