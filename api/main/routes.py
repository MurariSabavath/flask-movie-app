import requests
from flask import Blueprint, render_template, url_for, current_app, redirect, request
from .froms import SearchForm

main = Blueprint("main", __name__)

@main.route("/", methods=['POST', 'GET'])
@main.route("/home", methods=['POST', 'GET'])
def home():
    form = SearchForm()
    trending_week = requests.get(f"{current_app.config['URL']}trending/all/week?api_key={current_app.config['API_KEY']}").json()
    trending_day = requests.get(f"{current_app.config['URL']}trending/all/day?api_key={current_app.config['API_KEY']}").json()
    if form.validate_on_submit():
        data = request.form.get("search", None)
        return redirect(url_for("main.search", data=data))
    return render_template("home.html", title="Home", form=form, trending_week=trending_week, trending_day=trending_day)


@main.route("/results")
def search():
    if request.args:
        r = requests.get(f"{current_app.config['URL']}search/multi?api_key={current_app.config['API_KEY']}&language=en-US&query={request.args['data']}&page=1&include_adult=false").json()
        return render_template("search.html", title="Search", data=r)
    else:
        return render_template("search.html", title="Search")
