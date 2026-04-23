from flask import Flask, request, jsonify

app = Flask(__name__)

FLAGS = {
    "FLAG{player1}": "player1",
    "FLAG{player2}": "player2",
    "FLAG{player3}": "player3"
}

@app.route("/submit", methods=["POST"])
def submit_flag():
    data = request.get_json()
    flag = data.get("flag")

    if flag in FLAGS:
        return jsonify({
            "status": "success",
            "eliminated": FLAGS[flag]
        })
    
    return jsonify({
        "status": "error",
        "message": "invalid flag"
    }), 400

@app.route("/")
def home():
    return "KoTH server running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)