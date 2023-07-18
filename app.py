# app.py
from controllers.order_controller import orders_blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(orders_blueprint)

@app.route('/')
def index():
    return "<h1>My shop</h1>"