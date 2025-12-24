#!/usr/bin/python3
"""Flask app rendering a dynamic items list using Jinja logic."""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)


def load_items():
    """Load items list from items.json. Returns a list (possibly empty)."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "items.json")

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return []

    items = data.get("items")
    if isinstance(items, list):
        return items
    return []


@app.route("/items")
def items():
    """Render items.html with list of items from JSON file."""
    items_list = load_items()
    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
