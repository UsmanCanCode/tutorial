from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    user = "Usman"
    return render_template("home.html", name=user)


@app.route("/about")
def about():
    return render_template("about.html")


import learn
app.register_blueprint(learn.bp)

if __name__ == "__main__":
    app.run(debug=True)
