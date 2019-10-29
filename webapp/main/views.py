from flask import Blueprint, render_template
from flask_login import current_user, login_required

from webapp.auth.forms import MainForm

blueprint = Blueprint('main', __name__, url_prefix='/main')

@blueprint.route('/')
@login_required
def main():
    title = 'Добро пожаловать в личный кабинет.'
    main_form = MainForm()
    return render_template('auth/index.html', page_title=title, form=main_form)