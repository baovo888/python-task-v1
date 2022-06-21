import os
import argparse
import json

SUCCESS_STATUS = "Success"


def open_file(db="data.json"):
    with open(db) as fd:
        data = json.load(fd)
    return data


def update_database(updated_data, db="data.json"):
    with open(db, "w") as fd:
        json.dump(updated_data, fd)


def print_items(data):
    items = data["items"]
    for i, v in enumerate(items):
        print(f'{i+1}. {v["task"]} ({v["status"]})')


def add_item(new_task, db="data.json"):
    # Validation
    validate_add_input(new_task)

    updated_data = open_file(db)
    updated_data["items"].append(
        {
            "task": new_task,
            "status": "TO_DO"
        }
    )
    update_database(updated_data)
    return SUCCESS_STATUS


def complete_item(id, db="data.json"):
    data = open_file(db)
    # Validation
    validate_edit_id(data, id)

    # list index is offset by 1 with task id
    task_index = int(id) - 1
    updated_data = data.copy()
    # Update status to done on target task index
    target_task = updated_data["items"][task_index]
    target_task["status"] = "DONE"
    updated_data["items"][task_index] = target_task
    # Sync updated data
    update_database(updated_data)
    return SUCCESS_STATUS


def incomplete_item(id, db="data.json"):
    data = open_file(db)
    # Validation
    validate_edit_id(data, id)

    # list index is offset by 1 with task id
    task_index = int(id) - 1
    updated_data = data.copy()
    # Update status to done on target task index
    target_task = updated_data["items"][task_index]
    target_task["status"] = "TO_DO"
    updated_data["items"][task_index] = target_task
    # Sync updated data
    update_database(updated_data)
    return SUCCESS_STATUS


def delete_item(id, db="data.json"):
    data = open_file(db)
    # Validation
    validate_edit_id(data, id)
    # list index is offset by 1 with task id
    task_index = int(id) - 1
    updated_data = data.copy()
    # Remove task from list
    updated_data["items"].pop(task_index)
    # Sync updated data
    update_database(updated_data)
    return SUCCESS_STATUS


def get_all_items_with_task_index():
    data = open_file()
    for i, item in enumerate(data["items"]):
        data["items"][i]["id"] = str(i+1)
    return(data["items"])


def get_item_by_id(id):
    data = open_file()
    validate_edit_id(data, id)
    index = int(id) - 1  # Task id is offset by 1
    return(data["items"][index])


def validate_edit_id(data, id):
    if not isinstance(id, str):
        raise TypeError('The task id must be index number in string format')
    # Check if task list is not empty
    if len(data["items"]) == 0:
        raise ValueError('The task list is empty, cannot edit or delete')
    # Check id must be valid positive integer:
    if not id.isdigit():
        raise ValueError(
            'Invalid input provide. ID must be a valid digit number')
    # Check id must be in valid range
    if int(id) not in range(1, len(data["items"])+1):
        raise ValueError(
            f'Input ID is out of range. ID must be between 1 & {len(data["items"])}')


def validate_add_input(item):
    if not isinstance(item, str):
        raise TypeError("The task input must be string")
    if item.isspace():
        raise ValueError("Input task cannot be only blank space")
    if len(item) == 0:
        raise ValueError("Input task cannot be empty string")
