import unittest
import json
from task_api import app, tasks  # Import the Flask app and tasks list

class TaskAPITestCase(unittest.TestCase):
    """Unit tests for the Task Management API"""

    def setUp(self):
     """Set up a test client and reset tasks list before each test"""
     self.client = app.test_client()
     self.client.testing = True
     tasks.clear()  # Clear tasks before each test to avoid interference



    def test_get_tasks(self):
        """Test GET /tasks (should return an empty list at start)"""
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])  # Ensure tasks list is empty initially

    def test_add_task(self):
        """Test POST /tasks (adding a new task)"""
        response = self.client.post(
            "/tasks",
            data=json.dumps({"title": "Buy groceries"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json)
        self.assertEqual(response.json["task"]["title"], "Buy groceries")

    def test_update_task(self):
        """Test PUT /tasks/<id> (updating a task)"""
        # First, create a new task
        add_response = self.client.post(
            "/tasks",
            data=json.dumps({"title": "Buy groceries"}),
            content_type="application/json"
        )

        # Get the assigned task ID
        task_id = add_response.json["task"]["id"]

        # Now, update the correct task ID
        response = self.client.put(
            f"/tasks/{task_id}",
            data=json.dumps({"completed": True}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["task"]["completed"], True)

    def test_delete_task(self):
        """Test DELETE /tasks/<id> (deleting a task)"""
        # First, create a new task
        add_response = self.client.post(
            "/tasks",
            data=json.dumps({"title": "Buy groceries"}),
            content_type="application/json"
        )

        # Get the assigned task ID
        task_id = add_response.json["task"]["id"]

        # Now, delete the task
        response = self.client.delete(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Task deleted")

if __name__ == "__main__":
    unittest.main()
