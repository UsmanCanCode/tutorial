from flask import Blueprint, render_template

framework = {
    "flask": "A python framework to build web apps and api",
    "jinja2": "A templating engine to use python code with HTML"
}

bp = Blueprint('learn', __name__)


@bp.route("/learn/<something>")
def learn(something):
    learning = framework.get(something, "Nothing to learn")

    return render_template("learn.html", language=something, about=learning,
                           dictionary=framework)
