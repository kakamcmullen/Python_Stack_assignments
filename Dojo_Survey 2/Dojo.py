from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def form(name, location, language, comment):
    print "Form"
    return render_template('results.html')

@app.route('/survey', methods=['POST'])
def survey_completion():
    print "Got POST Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('results.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True)
