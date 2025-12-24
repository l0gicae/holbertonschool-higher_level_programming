#!/usr/bin/python3
"""Flask app to display products from JSON, CSV or SQLite based on query params."""
from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_products_from_json():
    """Load products from products.json. Returns a list of dicts."""
    path = os.path.join(BASE_DIR, "products.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return []

    if isinstance(data, list):
        return data
    return data.get("products", [])


def load_products_from_csv():
    """Load products from products.csv. Returns a list of dicts."""
    path = os.path.join(BASE_DIR, "products.csv")
    products = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(
                    {
                        "id": row.get("id"),
                        "name": row.get("name"),
                        "category": row.get("category"),
                        "price": row.get("price"),
                    }
                )
    except OSError:
        return []
    return products


def load_products_from_sql():
    """Load products from products.db (SQLite). Returns a list of dicts."""
    path = os.path.join(BASE_DIR, "products.db")
    products = []
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "category": row[2],
                    "price": row[3],
                }
            )
        conn.close()
    except sqlite3.Error:
        return []
    return products


@app.route("/products")
def products():
    """
    Display products from JSON, CSV or SQLite depending on ?source= param.

    Query parameters:
    - source: "json", "csv" or "sql"
    - id: optional product id to filter a single product
    """
    source = request.args.get("source")
    prod_id = request.args.get("id")
    error = None
    products_list = []

    if source == "json":
        products_list = load_products_from_json()
    elif source == "csv":
        products_list = load_products_from_csv()
    elif source == "sql":
        products_list = load_products_from_sql()
    else:
        error = "Wrong source"

    # Filter by id if provided and no prior error
    if error is None and prod_id:
        filtered = [p for p in products_list if str(p.get("id")) == str(prod_id)]
        if not filtered:
            error = "Product not found"
            products_list = []
        else:
            products_list = filtered

    return render_template(
        "product_display.html",
        products=products_list,
        error=error,
        source=source,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
