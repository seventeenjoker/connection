from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate

from webapp.admin.views import blueprint as admin_blueprint
from webapp.main.views import blueprint as main_blueprint
from webapp.auth.models import db, User, Person, PythagoreanSquare
from webapp.auth.models import User
from webapp.auth.views import blueprint as user_blueprint
from webapp.auth.forms import LoginForm

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(main_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
