import os
import requests
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("home.html")


@app.route('/discord/oauth/?code=<code>&state=<state>')
def authorized_discord():
    code = request.args.get("code")
    data = {
        "code": code,
        "client_id": os.environ.get("CLIENT_ID"),
        "client_secret": os.environ.get("CLIENT_SECRET"),
        "grant_type": "authorization_code",
        "redirect_uri": "https://czvr-role-bot.herokuapp.com/discord/success"
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post("https://discord.com/api/v8/oauth2/token", headers=header, data=data)
    print(r.json())


@app.route("/discord/success")
def discord_success():
    return render_template("discord_success.html")


try:
    app.run(None, 80)
except:
    pass
