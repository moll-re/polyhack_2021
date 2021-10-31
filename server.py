from flask import Flask, render_template, request, request, session
import random

from apis.interactive_maps import SwissMap
from models.user import Users
from models.event import Events
import plotly.graph_objects as go
from plotly.offline import plot

USERBASE = Users()
MAP = SwissMap()
EVENTBASE = Events()

import dummy_data
dummy_data.populate_data(USERBASE, EVENTBASE)
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
    days, co2_savings = [], []

    for e in user.travel_history:
        days.append(e.date.replace(day=1))
        co2_savings.append(e.co2_savings)

    fig = go.Figure()
    fig.layout.update(
        xaxis = {'showgrid': False},
        yaxis = {'showgrid': False},
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        colorway=["#D50505", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
    )
    fig.add_trace(go.Bar(x=days, y=co2_savings))
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    context = {
        "map_path" : MAP.travel_history_map(user.id, user.travel_history),
        "plotly_html" : plot_div
    }
    return render_template("user_detail.html", context=context, user=user)



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