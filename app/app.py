from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Hello from Flask App deployed via CI/CD on Kubernetes 🚀",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "dev")
    }

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

