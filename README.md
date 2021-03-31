# Flask Movie App
- A Flask app which is built using TMDB API with user authentication and watch list options. The data is generated from [TMDB API](https://developers.themoviedb.org/3/getting-started/introduction).
- [Click here](https://movie-app-flask.herokuapp.com/) to view the app.
# Requirements
- Python 3 should be installed in your machine.
- Required modules can be found in requirements.txt file.
# Installation and setup
- Start a virtual environment in your machine using `python-venv module` and activate the virtual environment
	>`python-venv` module and its documentation can be found [here](https://docs.python.org/3/tutorial/venv.html).
- Clone this repository using command `git clone https://github.com/MurariSabavath/flask-movie-app.git` in your command prompt/terminal.
- Change your current directory to `flask-movie-app` directory so that you are in flask-movie-app directory now.
- Enter `pip install -r requirements.txt` to download all required packages.
- Create a .env file `flask-movie-app` and add environment variables like
	>	`SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'` </br>
	> `URL = 'https://api.themoviedb.org/3/'` </br>
	> 	`SECRET_KEY = "YOUR SECRET KEY"`' </br>
	> `API_KEY = "YOUR API KEY"`
- Go to **[TMDB DEVELOPERS SITE](https://developers.themoviedb.org/3)** sign up and login to generate API KEY.
- Uncomment lines 6 and 8 in  `__ init__.py ` file which is  in `api` directory
- In `wsgi.py` file uncomment 4th line.
- Open the terminal and enter `python wsgi.py` command and open your browser to view app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
