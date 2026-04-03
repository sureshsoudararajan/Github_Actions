#flask
from flask import Flask

app = Flask(__name__)

@app.route('/home')  
def home():
    return "Hello"

@app.route('/about')
def about():
    return "About"
    
app.run(host="0.0.0.0", port=5008)
