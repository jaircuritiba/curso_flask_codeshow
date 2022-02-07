# Contextos - segue uma linha do tempo

from flask import Flask

app = Flask(__name__)

## 1 Configuração
### Add Configuração
app.config["DEBUG"] = "True"
app.config["SQLALCHEMY_DB_URI"] = "myysql://.." 

### Registar Rotas
@app.route("/path")

