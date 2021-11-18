from flask import Flask, render_template, url_for
from jinja2 import Template

app = Flask(__name__)

menu = ['Setup', 'First app', 'Feedback']

@app.route("/")
@app.route("/index")
def index():
    print( url_for('index'))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title='About our site', menu=menu)

if __name__ == "__main__":
    app.run(debug=True)



