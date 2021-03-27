from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegistrationForm
from api.models import User
from api import db, bcrypt
from flask_login import login_manager, login_user, logout_user, login_required, current_user

user = Blueprint('user', __name__)

@user.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(email=form.email.data, username=form.username.data, password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('You account has been creatd successfully', 'success')
        return redirect(url_for('main.home'))
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
            return redirect(url_for("main.home"))
        flash("Login unsuccessful!", 'error')
        return redirect(url_for("user.login"))
    return render_template("login.html", title="Login", form=form)

@user.route("/profile")
@login_required
def profile():
    return render_template("profile.html", title="Profile")

@user.route('/logout')
@login_required
def log_out():
    logout_user()
    flash("Logged out successfully!", 'success')
    return redirect(url_for("main.home"))