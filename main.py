
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


def print_items(data):
    items = data["items"]
    for i, v in enumerate(items):
        print(f'{i+1}. {v}')


def add_item(data, new_item):
    # Validate input item
    errorMsg = validate_add_input(new_item)
    if errorMsg != None:
        return errorMsg
    updated_data = data.copy()
    updated_data["items"].append(new_item)
    with open("data.json", "w") as fd:
        json.dump(updated_data, fd)
    return 'Success'


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
    # else:
    #   print('add is empty')
    print("--AFTER--")
    print_items(data)
    # print(args)
    # TODO: read arguments and determine what to do
    # TODO: write functions to deal with each argument


if __name__ == "__main__":
    main()
