from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_data():
    try:
        data = request.get_json(force=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON object"}), 400

        return jsonify({
            "status": "success",
            "message": "Payload processed safely",
            "data": data
        }), 200

    except Exception:
        return jsonify({"error": "Invalid request payload"}), 400


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

# pipeline trigger