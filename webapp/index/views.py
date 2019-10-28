from flask import Blueprint
from flask_login import current_user, login_required

blueprint = Blueprint('index', __name__, url_prefix='/index')

@blueprint.route('/')
@login_required
def index():
    return 'Здесь строится личный кабинет юзера.'