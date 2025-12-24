#!/usr/bin/python3
"""Flask app to display products from JSON or CSV based on query params."""
from flask import Flask, render_template, request
import json
import csv
import os

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

    # Expecting a list like: [{"id": ..., "name": ..., ...}, ...]
    if isinstance(data, list):
        return data
    # Or object with "products" key (fallback)
    return data.get("products", [])


def load_products_from_csv():
    """Load products from products.csv. Returns a list of dicts."""
    path = os.path.join(BASE_DIR, "products.csv")
    products = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Keep fields as strings; we will compare id as string.
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


@app.route("/products")
def products():
    """
    Display products from JSON or CSV depending on ?source= param.

    Query parameters:
    - source: "json" or "csv" (required)
    - id: optional product id (string or int), to filter a single product
    """
    source = request.args.get("source")
    prod_id = request.args.get("id")
    error = None
    products_list = []

    if source == "json":
        products_list = load_products_from_json()
    elif source == "csv":
        products_list = load_products_from_csv()
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
