from flask import Flask

from my_app.products.views import products

app = Flask(__name__)


# Importar vistas
app.register_blueprint(products)

@app.template_filter('mydouble')
def mydouble_filter(n:int):
    return n*2