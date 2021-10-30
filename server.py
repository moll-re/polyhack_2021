from flask import Flask, render_template, request, jsonify, make_response, request
import random
import time

from flask.templating import render_template_string

app = Flask(__name__)

heading = "Lorem ipsum dolor sit amet."

content = """
Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
Repellat inventore assumenda laboriosam, 
obcaecati saepe pariatur atque est? Quam, molestias nisi.
"""

db = list()  # The mock database

posts = 500  # num posts to generate

quantity = 20  # num posts to return per request


@app.route("/")
def index():
    """ Route to render the HTML """
    context = {
        "title" : f"Event title {id}",
        "image_name" : "fallback.jpg",
        "star_rating" : random.randint(1,4),
        "reviews" : random.randint(10,30),
        "user" : "Remy"
    }
    return render_template("base.html", context=context)



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