from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def LandingPage():
    return render_template('index.html')

@app.route('/ninja')
def turtles():
    return render_template('TURTLES.html')

@app.route('/ninja/<color>')
def ninjas(color):
    if color == "red":
        imgcolor = "raphael.jpg"
    elif color == "blue":
        imgcolor = "leonardo.jpg"
    elif color == "purple":
        imgcolor = "donatello.jpg"
    elif color == "orange":
        imgcolor = "michelangelo.jpg"
    else:
        imgcolor = "notapril.jpg"   
    print imgcolor
    return render_template('ninja.html', color = imgcolor)

@app.route('/Turtles')
def Turtles():
    return render_template('TURTLES.html')

app.run(debug=True)
