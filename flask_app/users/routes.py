import requests
from flask import Blueprint, render_template, redirect, url_for, flash, current_app, request
from .forms import LoginForm, RegistrationForm
from flask_app.models import User, WatchList
from flask_app import db, bcrypt
from flask_login import login_manager, login_user, logout_user, login_required, current_user
from flask_app.main.utils import watch_list_shows

user = Blueprint('user', __name__)

@user.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, username=form.username.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('You account has been created successfully', 'success')
        return redirect(url_for('user.login'))
    return render_template("register.html", title="Register", form=form)


@user.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if(user and bcrypt.check_password_hash(user.password, form.password.data)):
            login_user(user)
            flash("Logged into your account!", 'success')
            next = request.args.get('next')
            return redirect(next or url_for("main.home"))
        flash("Login unsuccessful!", 'error')
        return redirect(url_for("user.login"))
    return render_template("login.html", title="Login", form=form)

@user.route("/profile")
@login_required
def profile():
    list = WatchList.query.filter_by(user_id=current_user.id).all()
    shows = []
    movies = []
    for item in list:
        if(item.show):
            show_url = f"{current_app.config['URL']}tv/{item.show}?api_key={current_app.config['API_KEY']}&language=en-US"
            show = requests.get(show_url).json()
            shows.append(show)
        else:
            movie_url = f"{current_app.config['URL']}movie/{item.movie}?api_key={current_app.config['API_KEY']}&language=en-US"
            movie_data = requests.get(movie_url).json()
            movies.append(movie_data)
    return render_template("profile.html", title="Profile", shows=shows, movies=movies)

@user.route('/logout')
@login_required
def log_out():
    logout_user()
    flash("Logged out successfully!", 'success')
    return redirect(url_for("main.home"))

@user.route("/add/<string:m_type>/<int:m_id>")
@login_required
def add(m_type, m_id):
    user_movies, user_shows = [], []
    if current_user.is_authenticated:
        user_movies, user_shows = watch_list_shows(current_user.id)
        user = User.query.filter_by(id=current_user.id).first()
        if m_type == 'movie':
            if m_id not in user_movies:
                mv = WatchList(movie=m_id, user_id=user.id)
                db.session.add(mv)
                db.session.commit()
        else:
            if m_id not in user_shows:
                mv = WatchList(show=m_id, user_id=user.id)
                db.session.add(mv)
                db.session.commit()
    return redirect(request.referrer)
