from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import basedir

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='{%',
        block_end_string='%}',
        variable_start_string='[[',
        variable_end_string=']]',
        comment_start_string='{#',
        comment_end_string='#}',
    ))

db = SQLAlchemy()
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'

def create_app(config_name):
    app = CustomFlask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)
    lm.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

app = create_app('config')

from app import views, models