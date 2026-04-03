from flask import Flask

app = Flask(__name__)

@app.route('/home')  
def home():
    return "Hello"

@app.route('/about')
def about():
    return "Ab  out"

app.run(port=5008, debug=True)