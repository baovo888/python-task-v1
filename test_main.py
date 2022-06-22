"""
Test module for main.py
"""
import unittest
import main
import json


class Test_main(unittest.TestCase):
    API_URL = "http://127.0.0.1:8000"

    def setUp(self):
        app = main.create_flask_app()
        app.debug = True
        self.app = app.test_client()

    """
    Test homepage and Get task endpoint
    """
    def test_homepage_view(self):
        res = self.app.get("/")
        assert res.status_code == 200

    def test_nonexist_endpoint(self):
        res = self.app.get("/doesntexist")
        assert res.status_code == 404

    def test_todo_get_all(self):
        res = self.app.get("/todo")
        assert res.status_code == 200

    """
    Test Adding feature
    """
    def test_todo_add(self):
        payload = {"task": "new task"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = self.app.post("/todo/add",headers=headers, data=payload)
        assert res.status_code == 302

    def test_todo_add_with_empty_data(self):
        payload = {"task": ""}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = self.app.post("/todo/add",headers=headers, data=payload)
        assert res.status_code == 400

    def test_todo_add_with_spaces_only(self):
        payload = {"task": "   "}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = self.app.post("/todo/add",headers=headers, data=payload)
        assert res.status_code == 400

    """
    Test Completing feature
    """

    def test_completing_feature(self):
        # Add one new task to end of list
        payload = {"task": "TestTask"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.app.post("/todo/add", headers=headers, data=payload)

        # Get task ID of the new task
        res = self.app.get("/todo")
        last_task = json.loads(res.text)[-1]

        # Update task status on new task
        complete_res = self.app.post(f"/todo/complete/{last_task['id']}")

        # Get task ID of the new task
        res = self.app.get("/todo")
        last_task = json.loads(res.text)[-1]
        assert complete_res.status_code == 302
        assert last_task["status"] == "DONE"

        # Cleanup new task
        self.app.get(f"/todo/delete/{last_task['id']}")

    def test_completing_invalid_taskid(self):
        # Update task status on new task
        res = self.app.post("/todo/complete/9999")
        assert res.status_code == 400

    """
    Test Incompleting feature
    """

    def test_incompleting_feature(self):
        # Add one new task to end of list
        payload = {"task": "TestIncompleteTask"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.app.post("/todo/add", headers=headers, data=payload)

        # Get task ID of the new task
        res = self.app.get("/todo")
        last_task = json.loads(res.text)[-1]

        # Update task status on new task
        complete_res = self.app.post(f"/todo/complete/{last_task['id']}")

        # Test incomplete API
        incomplete_res = self.app.post(f"/todo/incomplete/{last_task['id']}")

        # Get task ID of the new task
        res = self.app.get("/todo")
        last_task = json.loads(res.text)[-1]
        assert incomplete_res.status_code == 302
        assert last_task["status"] == "TO_DO"

        # Cleanup new task
        self.app.get(f"/todo/delete/{last_task['id']}")

    def test_incompleting_invalid_taskid(self):
        # Update task status on new task
        res = self.app.post("/todo/incomplete/9999")
        assert res.status_code == 400

    """
    Test deleting feature
    """

    def test_delete_feature(self):
        # Add one new task to end of list
        payload = {"task": "TestIncompleteTask"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.app.post("/todo/add", headers=headers, data=payload)

        # Get task ID of the new task
        res = self.app.get("/todo")
        last_task = json.loads(res.text)[-1]

        # Test incomplete API
        delete_res = self.app.post(f"/todo/delete/{last_task['id']}")

        # Get task ID of the new task
        res = self.app.get("/todo")
        after_delete_last_task = json.loads(res.text)[-1]
        assert delete_res.status_code == 302
