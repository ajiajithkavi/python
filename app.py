from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import random
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=1)

# Dummy user data (replace with a database in a real-world scenario)
users = {
    "veera": {"password": "1234"},
    "arun": {"password": "9090"}
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["username"]
        password = request.form["password"]

        # Validate username and password
        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect(url_for("user"))
        else:
            return render_template("login.html", error="Invalid username or password")

    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True,port=5001)
