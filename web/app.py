"""
Lindsay Marean's Flask API.
"""

from flask import Flask, render_template, send_from_directory, abort
import os
import os.path


app = Flask(__name__)


@app.route("/")
def home():
    return return_page("index.html")
    return "UOCIS docker demo!\n"


@app.route("/<page>")
def return_page(page):
    # If a page starts with or includes one of the symbols(`~` `//` `..`), return 403 Forbidden
    if '//' in page or '..' in page or '~' in page:
        abort(403)
    # what's the path?
    path, filename = os.path.split(page)
    path = './pages/' + path
    if not (filename in os.listdir(path)):
        abort(404)
    if (page[-4:] != 'html') and (page[-3:] != 'css'):
        abort(404)
    return send_from_directory(path, page)  # pathname, filename


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
