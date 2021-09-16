from cs50 import SQL
from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

SPORTS = [
    "Dodgeball",
    "Cricket",
    "Soccer",
    "Hockey",
    "Chess"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST", "GET"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        return render_template("error.html", message="Missing name")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invaid sport")
    db.execute("INSERT INTO registrants (name,sport) VALUES (?, ?)", name, sport)
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")

    return render_template("registrants.html", registrants=registrants)
