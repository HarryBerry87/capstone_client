from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/camera/<int:cam_id>")
def album():
    return render_template('album.html', cam_id=cam_id)
