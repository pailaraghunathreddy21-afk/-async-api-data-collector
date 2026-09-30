from flask import Flask, render_template
import json
import os

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


if __name__ == "__main__":
    app.run(debug=True)