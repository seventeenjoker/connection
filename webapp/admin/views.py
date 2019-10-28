from flask import Blueprint
from flask_login import current_user, login_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@login_required
def admin():
    return 'Привет админ!' if current_user.is_admin else 'Ты не админ!'