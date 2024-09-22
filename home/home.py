from flask import Blueprint, render_template

inicio = Blueprint('home', __name__, template_folder='templates')
@inicio.route('/')
def home():
    return render_template('index.html')