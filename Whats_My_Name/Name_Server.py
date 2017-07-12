from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('name.html')

@app.route('/<your_name>')
def process(your_name):
    print request.form[""]
    return render_template('name.html')
app.run(debug=True)
