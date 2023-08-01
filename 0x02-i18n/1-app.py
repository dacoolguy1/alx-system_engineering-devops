#!/usr/bin/env python3
"""A Flask app that has a single route
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Config giles
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# lets instantiate the class
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index():
    """homepage route

    Returns:
        _type_: _description_
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
