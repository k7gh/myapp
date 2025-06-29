from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from your sample webserver!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return {"you_sent": data}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
