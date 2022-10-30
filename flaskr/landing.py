from flask import(
    Blueprint, render_template, url_for   
)

landing_bp = Blueprint('/', __name__, url_prefix='')

@landing_bp.route('/', methods=['GET'])
def landing():

    return render_template('landing.html')