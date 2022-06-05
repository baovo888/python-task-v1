
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
# - Write CD pipeline (GitHub Actions) to deploy to AWS

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

def main():
  data = open_file()

  parser = argparse.ArgumentParser()
  parser.add_argument("add", help="Adds a new item to the list")
  parser.add_argument("done", help="Marks an item has done")
  parser.add_argument("delete", help="Deletes an items from the list")
  args = parser.parse_args()

  # TODO: read arguments and determine what to do
  # TODO: write functions to deal with each argument

if __name__ == "__main__":
  main()