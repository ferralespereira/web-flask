from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "learning flask"


@app.route('/information')
@app.route('/information/<string:name>')
def information(name = None):

    if name:
        return f"<h1>information {name}</h1>"
    else:
        return f"<h1>information, do not have a name</h1>"


@app.route('/contact')
@app.route('/contact/<redirection>')
def contact(redirection = None):
    if redirection:
        return "<h1>contact</h1>"
    else:
        return redirect(url_for('information'))




if __name__ == '__main__':
    app.run(debug=True)

