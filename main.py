
# Author: Michael Crilly (upload.academy)
# Objective: write a simple todo list handler using Python + JSON
# Tasks:
# x Write all functions for handling all functionality
# x Use the JSON file as a database
# x Allow edits to the JSON file directly
# x Write unit tests for every function (unit)
# - Write a README.md file for the repository that documents the project
# x Write a CI pipeline (GitHub Actions) for running tests
# x Incorporate a Flask API to make the functionality avalable over HTTP(S)
# - Write tests to check HTTP handlers work
# - Write CD pipeline (GitHub Actions) to deploy to AWS

import argparse
from flask import Flask, jsonify, render_template, redirect, request
from flask_cors import CORS
import to_do
from to_do import delete_item, open_file, print_items, add_item, complete_item, delete_item


def create_flask_app(config=None):
    app = Flask(__name__)

    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Setup cors headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # Defaut route show all items
    @app.route("/")
    def show_tasks():
        try:
            items = to_do.get_all_items_with_task_index()
            return render_template("index.html", items=items)
        except Exception as error:
            return f"There was a problem loading this task - {error}", 400

    # Get all tasks
    @app.route("/todo", methods=["GET"])
    def get_all_tasks():
        try:
            jsonify(to_do.get_all_items_with_task_index())
        except Exception as error:
            return error, 400

    # Get task by id
    @app.route("/todo/<task_id>", methods=["GET"])
    def get_task_by_id(task_id):
        try:
            jsonify(to_do.get_item_by_id(task_id))
        except Exception as error:
            return error, 400

    # Add new task
    @app.route("/todo/add", methods=["POST"])
    def add_new_task():
        task = request.form['task']
        try:
            to_do.add_item(str(task))
            return redirect('/')
        except Exception as error:
            return f"There was a problem adding this task - {error}", 400

    # Update task as done
    @app.route("/todo/complete/<task_id>", methods=["POST", "GET"])
    def complete_task(task_id):
        try:
            to_do.complete_item(str(task_id))
            return redirect('/')
        except Exception as error:
            return f"There was a problem completing this task - {error}", 400

    # Update task as incomplete
    @app.route("/todo/incomplete/<task_id>", methods=["POST", "GET"])
    def incomplete_task(task_id):
        try:
            to_do.incomplete_item(str(task_id))
            return redirect('/')
        except Exception as error:
            return f"There was a problem completing this task - {error}", 400

    # Delete task

    @app.route("/todo/delete/<task_id>")
    def delete_task(task_id):
        try:
            to_do.delete_item(str(task_id))
            return redirect('/')
        except Exception as error:
            return f"There was a problem delete this task - {error}", 400

    return app


def main():
    data = open_file()

    parser = argparse.ArgumentParser()
    parser.add_argument("--add", help="Adds a new item to the list")
    parser.add_argument("--done", help="Enter task ID to mark an item as done")
    parser.add_argument(
        "--delete", help="Enter task ID to delete an item from the list")
    args = parser.parse_args()

    if(args.add):
        task_status = add_item(args.add, data)
        print(task_status)
    if(args.done):
        task_status = complete_item(args.done, data)
        print(task_status)
    if(args.delete):
        task_status = delete_item(args.delete, data)
        print(task_status)

    parser.add_argument("-p", "--port", action="store", default="8000")

    args = parser.parse_args()
    port = int(args.port)
    app = create_flask_app()
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
