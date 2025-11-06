from flask import Blueprint, render_template

home_routes = Blueprint("home", __name__)

@home_routes.route('/')
def home():
    return render_template('index.html')