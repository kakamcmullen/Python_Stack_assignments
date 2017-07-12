from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

@app.route('/new', methods=['POST'])
def new():
    print "Got POST info"
    name = request.form['name']
    email = request.form['email']
    return render_template('dojos.html')

@app.route('/stylesheet')
def stylesheet():
    return render_template('stylesheet.css')
app.run(debug=True)
