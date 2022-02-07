import view
from flask import Flask

def create_app():
    """ Factory Principal """
    app = Flask(__name__)
    view.init_app(app)
    return app
