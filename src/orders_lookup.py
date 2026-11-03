import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/orders")
def find_orders():
    customer = request.args.get("customer")
    connection = sqlite3.connect("orders.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, total FROM orders WHERE customer = '" + customer + "'")
    return {"orders": cursor.fetchall()}
