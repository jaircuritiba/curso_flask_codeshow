from flask import Flask

""" Extensão Flask """

def init_app(app: Flask):
    """ inicialização de extensões """
    @app.route('/')
    def index():
        return "Hello Codeshow"

    @app.route('/contato')
    def contato():
        return "<form> <input type = 'text'></input></form>"

