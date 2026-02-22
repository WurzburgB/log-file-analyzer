from flask import Flask, render_template, request
import os
from parser import parse_logs

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    logs = []

    if request.method == "POST":
        file = request.files["logfile"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            logs = parse_logs(filepath)

    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(debug=True)