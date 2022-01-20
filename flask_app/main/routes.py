import requests
from flask import Blueprint, render_template, url_for, current_app, redirect, request
from flask_login import current_user
from .froms import SearchForm
from .utils import watch_list_shows

main = Blueprint("main", __name__)

@main.route("/", methods=['POST', 'GET'])
@main.route("/home", methods=['POST', 'GET'])
def home():
    form = SearchForm()
    trending_week = requests.get(f"{current_app.config['URL']}trending/all/week?api_key={current_app.config['API_KEY']}").json()
    trending_day = requests.get(f"{current_app.config['URL']}trending/all/day?api_key={current_app.config['API_KEY']}").json()
    user_movies, user_shows = [], []
    if current_user.is_authenticated:
        user_movies, user_shows = watch_list_shows(current_user.id)
    if form.validate_on_submit():
        data = request.form.get("search", None)
        return redirect(url_for("main.search", data=data))
    return render_template("home.html", title="Home", form=form, trending_week=trending_week, \
        trending_day=trending_day, user_movies=user_movies, user_shows=user_shows)


@main.route("/results")
def search():
    user_movies, user_shows = [], []
    if current_user.is_authenticated:
        user_movies, user_shows = watch_list_shows(current_user.id)
    if request.args:
        r = requests.get(f"{current_app.config['URL']}search/multi?api_key={current_app.config['API_KEY']}&language=en-US&query={request.args['data']}&page=1&include_adult=false").json()
        return render_template("search.html", title="Search", data=r, user_movies=user_movies, user_shows=user_shows)
    else:
        return render_template("search.html", title="Search", user_movies=user_movies, user_shows=user_shows)
