from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/goodbye_world')
def goodbye_world():
    return 'goodbye, World!'

@app.route('/noisebridge')
def noisebridge():
    return 'noisebridge'
