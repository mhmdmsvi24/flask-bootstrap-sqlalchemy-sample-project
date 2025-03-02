from flask import render_template


def page_not_found(e):
    return render_template("index.html", error="404"), 404


def internal_server_error(e):
    return render_template("index.html", error="500"), 500
