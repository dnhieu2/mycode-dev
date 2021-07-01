#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

#list of questions and answers
trivia = {question: ""}


@app.route("/")
def rootdirect:
    return

## This is where we want to redirect users
@app.route("/<name>")
def isitsuccessful(name):
    if name == "":
        return redirect(url_for("hello_admin")
    else:
        return redirect(url_for("hello_guest", guesty = name)


# This is a landing point for users (a start)
@app.route("/") # user will land at "/"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("answer"): # if nm was assigned via the POST
            answer = request.form.get("answer") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value
            answer = "Invalid answer. Please try again."
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("answer"): # if nm was assigned as a parameter=value
            answer = request.args.get("answer") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            answer = "Invalid answer. Please try again." # ...then user is just defaultuser
    return redirect(url_for("success", name = answer)) # pass back to /success with val for name
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

