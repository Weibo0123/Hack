from flask import Flask, request, jsonify
import docker

app = Flask(__name__)

client = docker.from_env()

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
        target = FLAGS[flag]
        
        try:
            container = client.containers.get(target)
            container.stop()
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500
        
        return jsonify({
            "status": "success",
            "eliminated": target
        })

    return jsonify({
        "status": "error",
        "message": "invalid flag"
    }), 400

@app.route("/")
def home():
    return "Hack server running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)