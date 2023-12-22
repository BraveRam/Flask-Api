from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' 

@app.route('/api')
def res():
    return 'Flask Api - deployed to vercel' 
