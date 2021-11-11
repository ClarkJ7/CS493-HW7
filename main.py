from google.cloud import datastore
from flask import Flask, request, render_template, request, url_for, redirect
import requests
import random
import string

app = Flask(__name__)
client = datastore.Client()

client_id = "942293111488-9do4e7f5h5mpgu6q4qvciji1po22ijbg.apps.googleusercontent.com"
client_secret = "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"
google_people_api = "https://people.googleapis.com/v1/people/me?personFields=names"
google_Oauth_endpoint = "https://accounts.google.com/o/oauth2/v2/auth?"
google_Oauth_post = "https://www.googleapis.com/oauth2/v4/token"
local_redirect = "http://localhost:8080/oauth"
deployed_redirect = "https://oauth-330917.uw.r.appspot.com/oauth"


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/boats', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html')


@app.route('/owners/<owner_id>/boats', methods=['GET'])
def index():
    return render_template('welcome.html')


@app.route('/boats/<boat_id>', methods=['DELETE'])
def index():
    return render_template('welcome.html')