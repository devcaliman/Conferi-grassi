from flask import Flask, jsonify
import sqlite3
con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"Api iniciado com exito!"})

if __name__ == "__main__":
    app.run(debug=True)
