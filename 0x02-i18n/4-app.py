#!/usr/bin/env python3
"""4-app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """class configuration"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """route to index page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
