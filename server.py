from flask import Flask, render_template, request, request, session
import random

from apis.interactive_maps import SwissMap
from models.user import Users

USERBASE = Users()
USERBASE.add_user(id=239842123, name="Remy", event_preferences=["hiking","skiing"], event_blacklist = [], home_coordinates=[0,0], group_size=1, min_age=20, max_age=20)
MAP = SwissMap()

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/")
def index():
    session["user_id"] = 239842123 # a perfectly safe login, hem hem
    context = {
        "title" : f"Event title {id}",
        "image_name" : "fallback.jpg",
        "star_rating" : random.randint(1,4),
        "reviews" : random.randint(10,30),
        "user" : USERBASE.get_by_id(session["user_id"]).name
    }
    return render_template("event_overview.html", context=context)



@app.route("/profile")
def profile():
    uid = session["user_id"]
    user = USERBASE.get_by_id(uid)

    context = {
        "map_path" : MAP.travel_history_map(user.id, user.travel_history)
    }
    return render_template("user_detail.html", conbtext=context, user=user)



@app.route("/get_event")
def get_event():
    id = request.args.get("id", type = int)
    context = {
        "title" : f"Event title {id}",
        "image_name" : "fallback.jpg",
        "star_rating" : random.randint(1,4),
        "reviews" : random.randint(10,30),
        "user" : "Remy"
    }
    return render_template("event_card.html", context=context)



app.run(port=8000, debug=True)