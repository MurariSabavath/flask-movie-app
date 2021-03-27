import requests
from flask import Blueprint, render_template, url_for, current_app, redirect, request

movies = Blueprint("movies", __name__)

@movies.route("/movie")
@movies.route("/movie/popular")
def movie():
    popular_url = f"{current_app.config['URL']}movie/popular?api_key={current_app.config['API_KEY']}&language=en-US&page=1"
    movies = requests.get(popular_url).json()
    heading = "Popular Movies"
    return render_template("movies.html", title="Popular Moives", movies=movies, heading=heading)


@movies.route("/movie/top-rated")
def top_rated():
    popular_url = f"{current_app.config['URL']}movie/top_rated?api_key={current_app.config['API_KEY']}&language=en-US&page=1"
    movies = requests.get(popular_url).json()
    heading = "Top Rated Movies"
    return render_template("movies.html", title="Top Rated", movies=movies, heading=heading)

@movies.route("/movie/<int:movie_id>")
def current_movie(movie_id):
    movie_url = f"{current_app.config['URL']}movie/{movie_id}?api_key={current_app.config['API_KEY']}&language=en-US"
    movie_data = requests.get(movie_url).json()
    return render_template("current_movie.html", title=movie_data['title'], movie=movie_data)