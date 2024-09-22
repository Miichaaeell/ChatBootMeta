from flask import Flask
from boot.boot import boot
from home.home import inicio

app = Flask(__name__)
app.register_blueprint(boot)
app.register_blueprint(inicio)
if __name__ == '__main__':
    app.run(debug=True)

