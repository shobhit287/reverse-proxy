from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def start():
    return jsonify({"message": "server is running"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
