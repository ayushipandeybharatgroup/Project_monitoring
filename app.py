from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "return "CI/CD working 🚀""

@app.route("/slow")
def slow():
    time.sleep(2)
    return "slow response"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
