from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return " Welcome to Flask HTTP Server!"

@app.route("/about")
def about():
    return "ℹ This is the About Page"

@app.route("/api")
def api():
    return jsonify({"message": "This is the API endpoint", "status": "success"})

@app.route("/user/<username>")
def user_profile(username):
    return jsonify({"message": f"Hello, {username}!", "status": "success"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
