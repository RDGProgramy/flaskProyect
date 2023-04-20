from flask import Flask

from my_app.products.views import products

app = Flask(__name__)


# Importar vistas
app.register_blueprint(products)

