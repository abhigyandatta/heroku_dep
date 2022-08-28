from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return ('Weird Flask')

@app.route('/cricket') 
def cricket():
    return ('Cricket World Cup')

@app.route('/login')
def login():
    return('Please enter login credentials:')       

app.run(debug=True)