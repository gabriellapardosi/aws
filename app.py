from flask import Flask, jsonify, request

app = Flask(__name__)

jurusan = [
    {"id": 1, "name": "gabriella lady rissa pardosi", "major": "Sistem Informasi", "nim": "2119113946"},
]

def _find_next_id():
    return max(jurusan["id"] for jurusan in jurusan) + 1

@app.route("/jurusan", methods=['GET'])
def get_jurusan():
    return jsonify(jurusan)

@app.route("/jurusan", methods=['POST'])
def add_jurusan():
    if request.is_json:
       new_jurusan = request.get_json()
       new_jurusan["id"] = _find_next_id()
       jurusan.append(new_jurusan)
       return new_jurusan, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == "__main__":
    app.run(debug=True, port=5000)
