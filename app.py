from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized and deployed to Heroku'

if __name__ == '__main__':
    app.run(host='https://circuitflow.herokuapp.com/', port=80)
