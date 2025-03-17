import time,logging
from flask import Flask,jsonify,request
app=Flask(__name__)
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(message)s")
def log_request():
    logging.info("Request from {request.remote_addr} -> {request.method} {request.path}")

API_KEY="my_secure_api_key"

def authenticate():
    if request.path.startswith("/api"):
        api_key=request.headers.get("X-API-KEY")
        if not api_key or api_key!=API_KEY:
            return jsonify({"error":"Unauthorized"}),401

@app.route("/")
def home():
    return("welcome to flask http server with middleware")
@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/api/data")
def api_data():
    return jsonify({"message": "Secure API data", "status": "success"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)