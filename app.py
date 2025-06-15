from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

FLAG = "TI404{S3m3stEr_3mP4t_mnT4p}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    connections = data.get("connections", [])

    # Konversi list of lists jadi set of tuples
    connections_set = set(tuple(conn) for conn in connections)
    required = {(1, 3), (3, 5)}

    if required.issubset(connections_set):
        return jsonify({"success": True, "flag": FLAG})
    else:
        return jsonify({"success": False})

if __name__ == '__main__':
    app.run(debug=True)
