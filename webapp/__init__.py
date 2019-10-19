from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from webapp.user.models import db, User, Person, PythagoreanSquare
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.user.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @app.route('/admin')
    @login_required
    def admin():
        if current_user.is_admin:
            return 'Привет админ.'
        else:
            return 'Ты не админ'

    @app.route('/index')
    def index():
        return 'Здесь строится личный кабинет юзера.'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
