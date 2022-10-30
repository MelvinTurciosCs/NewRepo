from flask import(
    Blueprint, render_template,
)

landing_bp = Blueprint('/', __name__, url_prefix='')

@landing_bp.route('/', methods=['GET'])
def landing():

    return render_template('landing.html')

@landing_bp.route('/home', methods=['GET'])
def home():

    return render_template('home.html')