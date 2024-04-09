#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """get_locale function"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
