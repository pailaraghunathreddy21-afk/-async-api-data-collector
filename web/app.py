from flask import Flask, render_template, redirect, url_for
import json
import os
import asyncio

from src.collector import collect_all_pages


app = Flask(__name__)


@app.route("/")
def home():
    data_file = "data/posts.json"

    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            data = json.load(file)
    else:
        data = []

    return render_template(
        "index.html",
        data=data,
        total_records=len(data),
        unique_records=len({item["id"] for item in data})
    )


@app.route("/collect")
def collect_data():
    all_data = asyncio.run(collect_all_pages())

    with open("data/posts.json", "w") as file:
        json.dump(all_data, file, indent=4)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)