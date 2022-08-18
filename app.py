import os
from pyexpat import model
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key 

@app.route("/", methods=("GET", "POST"))
def index():

    if request.method == "POST": 

        food = request.form["animal"]

        if food != "":
            completedprompt = generate_prompt(food)
        else:
            completedprompt = generate_prompt("main dish")

        #return redirect(url_for("index", result=completedprompt))

        return render_template("index.html", result=completedprompt)

    return render_template("index.html", result=generate_prompt("main dish"))
    
def generate_prompt(food):

    #food = "main dish"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=(f"create a name for a crazy complex new type of dish involing {food}, and a description of the {food}"),
        temperature=0.9,
        max_tokens = 100,
        presence_penalty = 2.0,
    )
    return (response.choices[0].text)

