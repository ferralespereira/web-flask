from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/information')
@app.route('/information/<string:name>')
def information(name = None):

    text = "<strong>information, do not have a name</strong>"
    if name:
        text = f"<h1>information {name}</h1>"

    return render_template('information.html', 
                            text=text
                            )




@app.route('/contact')
@app.route('/contact/<redirection>')
def contact(redirection = None):
    if redirection:
        return "<h1>contact</h1>"
    else:
        return redirect(url_for('information'))




if __name__ == '__main__':
    app.run(debug=True)

