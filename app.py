from flask import Flask, jsonify



app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"mensagem": "Api iniciou com sucesso"})


if __name__ == "__main__":
    
    app.run( port=3000, debug=True)