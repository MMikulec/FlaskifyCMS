# modules/blog/routes.py
from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix="/b")


@bp.route('/')
def blog_index():
    return "Blog module"
