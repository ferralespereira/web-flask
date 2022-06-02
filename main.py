from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "learning flask"

@app.route('/information/<string:name>/<string:last_name>')
def information(name, last_name):
    return f"<h1>information {name} {last_name}</h1>"

@app.route('/contact')
def contact():
    return "<h1>contact</h1>"

if __name__ == '__main__':
    app.run(debug=True)

