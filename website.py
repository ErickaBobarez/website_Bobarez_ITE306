from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/Page1")
def Page1():
    return render_template("Page1.html")


@app.route("/Page2")
def Page2():
    return render_template("Page2.html")


@app.route("/Page3")
def Page3():
    return render_template("Page3.html")


if __name__ == "__main__":
    app.run()
