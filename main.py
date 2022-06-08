
# Author: Michael Crilly (upload.academy)
# Objective: write a simple todo list handler using Python + JSON
# Tasks:
# - Write all functions for handling all functionality
# - Use the JSON file as a database
# - Allow edits to the JSON file directly
# - Write unit tests for every function (unit)
# - Write a README.md file for the repository that documents the project
# - Write a CI pipeline (GitHub Actions) for running tests
# - Incorporate a Flask API to make the functionality avalable over HTTP(S)
# - Write tests to check HTTP handlers work
# - Write CD pipeline (GitHub Actions) to deploy to
import json
import argparse


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
    return 'Success - Add new task'


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

    return f'Success - Complete Task #{id}'


def delete_item(data, id):
    # Validate input id
    errorMsg = validate_edit_id(data, id)
    if errorMsg != None:
        return errorMsg
    # list index is offset by 1 with task id
    task_index = int(id) - 1
    updated_data = data.copy()
    # Remove task from list
    updated_data["items"].pop(task_index)
    # Sync updated data
    update_file(updated_data)


def validate_edit_id(data, id):
    errorMsg = None
    # Check if task list is not empty
    if len(data["items"]) == 0:
        errorMsg = 'Task list is empty'
    # Check id must be valid positive integer:
    elif not id.isdigit():
        errorMsg = 'Invalid input provide. ID must be a valid digit number'
    # Check id must be in valid range
    elif int(id) not in range(1, len(data["items"])+1):
        errorMsg = f'Input ID is out of range. ID must be between 1 & {len(data["items"])}'
    return errorMsg


def validate_add_input(item):
    errorMsg = None
    if type(item) != str:
        errorMsg = "Add input must be in string format"
    elif item.isspace():
        errorMsg = "Input task cannot be empty string or only blank space"
    return errorMsg


def main():
    data = open_file()

    parser = argparse.ArgumentParser()
    parser.add_argument("--add", help="Adds a new item to the list")
    parser.add_argument("--done", help="Marks an item has done")
    parser.add_argument("--delete", help="Deletes an items from the list")
    args = parser.parse_args()
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
    # else:
    #   print('add is empty')
    print("--AFTER--")
    print_items(data)
    # print(args)
    # TODO: read arguments and determine what to do
    # TODO: write functions to deal with each argument


if __name__ == "__main__":
    main()
