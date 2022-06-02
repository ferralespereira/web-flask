from flask import Flask

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
def contact():
    return "<h1>contact</h1>"

if __name__ == '__main__':
    app.run(debug=True)

