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

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
