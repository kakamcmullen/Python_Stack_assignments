from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Hello_World():
    return render_template('hello_world.html')

app.run(debug=True)
