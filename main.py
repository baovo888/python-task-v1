
# Author: Michael Crilly (upload.academy)
# Objective: write a simple todo list handler using Python + JSON
# Tasks:
# x Write all functions for handling all functionality
# x Use the JSON file as a database
# x Allow edits to the JSON file directly
# x Write unit tests for every function (unit)
# - Write a README.md file for the repository that documents the project
# - Write a CI pipeline (GitHub Actions) for running tests
# - Incorporate a Flask API to make the functionality avalable over HTTP(S)
# - Write tests to check HTTP handlers work
# - Write CD pipeline (GitHub Actions) to deploy to
import json
import argparse
import string

SUCCESS_STATUS = "Success"

def open_file():
    with open("data.json") as fd:
        data = json.load(fd)

    return data


def update_file(updated_data):
    with open("data.json", "w") as fd:
        json.dump(updated_data, fd)


def print_items(data):
    items = data["items"]
    for i, v in enumerate(items):
        print(f'{i+1}. {v["task"]} ({v["status"]})')


def add_item(data, new_task):
    print(data)
    print(type(data))
    # Validate input item
    errorMsg = validate_add_input(new_task)
    if errorMsg != None:
        return errorMsg
    updated_data = data.copy()
    updated_data["items"].append(
        {
            "task": new_task,
            "status": "TO_DO"
        }
    )
    update_file(updated_data)
    return SUCCESS_STATUS


def complete_item(data, id):
    # Validate input id
    errorMsg = validate_edit_id(data, id)
    if errorMsg != None:
        return errorMsg

    # list index is offset by 1 with task id
    task_index = int(id) - 1
    updated_data = data.copy()
    # Update status to done on target task index
    target_task = updated_data["items"][task_index]
    target_task["status"] = "DONE"
    updated_data["items"][task_index] = target_task
    # Sync updated data
    update_file(updated_data)

    return SUCCESS_STATUS


def delete_item(data, id):
    # Validate input id
    validate_edit_id(data, id)
    # list index is offset by 1 with task id
    task_index = int(id) - 1
    updated_data = data.copy()
    # Remove task from list
    updated_data["items"].pop(task_index)
    # Sync updated data
    update_file(updated_data)

    return SUCCESS_STATUS


def validate_edit_id(data, id):
    if not isinstance(id, str):
        raise TypeError('The task id must be index number in string format')

    # Check if task list is not empty
    if len(data["items"]) == 0:
        raise ValueError('The task list is empty, cannot edit or delete')

    # Check id must be valid positive integer:
    if not id.isdigit():
        raise ValueError('Invalid input provide. ID must be a valid digit number')

    # Check id must be in valid range
    if int(id) not in range(1, len(data["items"])+1):
        raise ValueError(f'Input ID is out of range. ID must be between 1 & {len(data["items"])}')


def validate_add_input(item):
    if not isinstance(item, str):
        raise TypeError("The task input must be string")
    if item.isspace():
        raise ValueError("Input task cannot be only blank space")
    if len(item) == 0:
        raise ValueError("Input task cannot be empty string")


def main():
    data = open_file()

    parser = argparse.ArgumentParser()
    parser.add_argument("--add", help="Adds a new item to the list")
    parser.add_argument("--done", help="Enter task ID to mark an item as done")
    parser.add_argument("--delete", help="Enter task ID to delete an item from the list")
    args = parser.parse_args()
    # DONE: read arguments and determine what to do
    # DONE: write functions to deal with each argument
    print("--BEFORE--")
    print_items(data)
    if(args.add):
        task_status = add_item(data, args.add)
        print(task_status)
    if(args.done):
        task_status = complete_item(data, args.done)
        print(task_status)
    if(args.delete):
        task_status = delete_item(data, args.delete)
        print(task_status)
    print("--AFTER--")
    print_items(data)



if __name__ == "__main__":
    main()
