from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}


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

    REGISTRANTS[name] = sport
    print(REGISTRANTS)
    return render_template("registrants.html", registrants=REGISTRANTS)
