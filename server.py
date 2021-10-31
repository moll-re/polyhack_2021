from flask import Flask, render_template, request, request, session, abort
import plotly.graph_objects as go
from plotly.offline import plot


from apis.interactive_maps import SwissMap
from apis.weather import WeatherScoreCalculator
from models.user import Users
from models.event import Events

USERBASE = Users()
MAP = SwissMap()
EVENTBASE = Events()
WEATHERCALCULATOR = WeatherScoreCalculator()
import dummy_data
dummy_data.populate_data(USERBASE, EVENTBASE)



app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/")
def index():
    session["user_id"] = 239842123 # a perfectly safe login, hem hem
    user = USERBASE.get_by_id(session["user_id"])
    wscore = WEATHERCALCULATOR.calc_weather_score(EVENTBASE.get_by_id(1))
    wscore = 10 # hard coded for positive pitch experience
    weather_icon = ["☀️","🌥️","🌧️","⛈️"][int(wscore/25)]
    weather_string = ["looks great!", "could be better..."][int(wscore/50)]


    EVENTBASE.filter_events(user, wscore)

    
    context = {
        "user" : user.name,
        "weather_emoji" : weather_icon,
        "weather_string" : weather_string
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
    fig.update_yaxes(
        title_text = "Kg of CO2 saved",
        title_standoff = 5)
    fig.add_trace(go.Bar(x=days, y=co2_savings))
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    context = {
        "map_path" : MAP.travel_history_map(user.id, user.travel_history),
        "plotly_html" : plot_div
    }
    return render_template("user_detail.html", context=context, user=user)


@app.route("/get_event")
def get_event():
    eid = request.args.get("id", type = int)
    event = EVENTBASE.get_by_id(eid)
    if event:
        return render_template("event_card.html", event=event)
    else:
        abort(404)


@app.route("/event/<event_id>")
def event_detail(event_id):
    event = EVENTBASE.get_by_id(int(event_id))
    if event:
        return render_template("event_detail.html", event=event)
    else:
        abort(404)

@app.route("/event/<event_id>/booked")
def event_booked_view(event_id):
    uid = session["user_id"]
    event = EVENTBASE.get_by_id(int(event_id))
    user = USERBASE.get_by_id(int(uid))
    user.travel_history.append(event)
    if event:
        return render_template("event_booked.html", event=event)
    else:
        abort(404)


#############################
## And, liftoff!
app.run(host="0.0.0.0",port=8000, debug=True)