from flask import Blueprint, render_template
# TODO: werkzeug.exceptions es necesario apra importar la funcion abort,
# En el curso esta desactualizado o se esta utilizando una version antiguan en el proyecto
from werkzeug.exceptions import abort


from my_app.products.model.products import PRODUCTS

products = Blueprint('products', __name__)


@products.route('/')
@products.route('/home')
def index():
    return render_template('products/index.html', products = PRODUCTS)


@products.route('/show/<int:id>')
def show(id):
    product = PRODUCTS.get(id)
    if not product:
        abort(401)

    return render_template('products/show.html', products = product)
    