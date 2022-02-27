from flask import Blueprint, render_template

bp = Blueprint('news', __name__, url_prefix='/news')

@bp.route('/')
def home():
    return 'Hello World'