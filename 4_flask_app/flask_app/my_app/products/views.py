from flask import Blueprint, render_template
from my_app.products.model.products import PRODUCTS

products = Blueprint('products', __name__)


@products.route('/')
@products.route('/home')
def index():
    print(PRODUCTS.get(2))
    return render_template('products/index.html', products = PRODUCTS)
    