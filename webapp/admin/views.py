from webapp.user.decorators import admin_required
from flask import Blueprint

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@admin_required
def admin_index():
    return 'Привет админ'
