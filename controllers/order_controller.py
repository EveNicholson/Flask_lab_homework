from flask import render_template, Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint("Orders", __name__)


@orders_blueprint.route('/orders')
def index():
    return render_template("index.html", title="Order", order_list=orders)

