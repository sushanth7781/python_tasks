import requests

url = "http://127.0.0.1:8000/tasks"
headers = {"Content-Type": "application/json"}
data = {"title": "Buy groceries"}

response = requests.post(url, json=data, headers=headers)
print(response.json())  
