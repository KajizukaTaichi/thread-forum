from flask import Flask, render_template, request

app = Flask("スレッド")

@app.route("/")
def index():
    return render_template("index.html", log=open("log.txt", encoding="utf-8").read())

@app.route("/", methods=["POST"])
def indes():
    name: str = request.form["name"]
    msg: str = request.form["msg"]
    open("log.txt", mode="a", encoding="utf-8").write(f"[{name}]: {msg}\n")
    return render_template("index.html", log=open("log.txt", encoding="utf-8").read())

app.run(host="0.0.0.0", port=8080, debug=True)