from flask import Flask

app = Flask(__name__)

# Importar vistas

import my_app.hello1.views
import my_app.hello2.views