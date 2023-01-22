#Gurraj Singh 2023
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        image = request.form.get("image")
        response = openai.Image.create( #implementation of the OpenAI image generation API
        prompt= image,n=1,size="512x512")
        image_url = response['data'][0]['url']
        return redirect(url_for("index", result = image_url))
    result = request.args.get("result")
    return render_template("index.html", result = result)
