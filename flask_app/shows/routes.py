import requests
from flask import Blueprint, render_template, url_for, current_app, redirect, request
from flask_login import current_user
from flask_app.main.utils import watch_list_shows

tv = Blueprint("tv", __name__)

@tv.route("/tv")
@tv.route("/tv/popular")
def show():
    user_movies, user_shows = [], []
    if current_user.is_authenticated:
        user_movies, user_shows = watch_list_shows(current_user.id)
    popular_url = f"{current_app.config['URL']}tv/popular?api_key={current_app.config['API_KEY']}&language=en-US&page=1"
    tv = requests.get(popular_url).json()
    heading = "Popular on TV"
    return render_template("tv.html", title="Popular Moives", tv=tv, heading=heading, user_shows=user_shows)


@tv.route("/tv/top-rated")
def top_rated():    
    user_movies, user_shows = [], []
    if current_user.is_authenticated:
        user_movies, user_shows = watch_list_shows(current_user.id)
    popular_url = f"{current_app.config['URL']}tv/top_rated?api_key={current_app.config['API_KEY']}&language=en-US&page=1"
    tv = requests.get(popular_url).json()
    heading = "Top Rated on TV"
    return render_template("tv.html", title="Top Rated", tv=tv, heading=heading, user_shows=user_shows)


@tv.route("/tv/<int:tv_id>")
def current_show(tv_id):
    show_url = f"{current_app.config['URL']}tv/{tv_id}?api_key={current_app.config['API_KEY']}&language=en-US"
    show = requests.get(show_url).json()
    return render_template("current_show.html", title=show['name'], show=show)
