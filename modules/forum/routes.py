# modules/forum/routes.py
from flask import Blueprint

bp = Blueprint('forum', __name__, url_prefix="/f")


@bp.route('/')
def forum_index():
    return "Forum module"
