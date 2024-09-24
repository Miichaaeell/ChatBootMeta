from flask import Flask
from boot.bot import robo
from home.home import inicio
from atendimento.atendimento import atendimento
from flask_login import LoginManager
from models.clientes import Funcionario, session
from os import getenv
secret_key = getenv('secret_key')

app = Flask(__name__)
app.secret_key = secret_key
login_manager = LoginManager(app)
@login_manager.user_loader
def get_user(user_id):
    return session.query(Funcionario).filter_by(id=user_id).first()
login_manager.blueprint_login_views = {'atendimento':'atendimento.login'}
app.register_blueprint(robo)
app.register_blueprint(inicio)
app.register_blueprint(atendimento)
if __name__ == '__main__':
    app.run(debug=True)

