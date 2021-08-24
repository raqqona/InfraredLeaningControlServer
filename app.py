from Flask import Flask, request, Response, make_response
import sqlite3
import os

app = Flask(__name__)

@app.errorhandler(500)
def error_500(error):
    return 500

@app.route('/api/pohling', method=['GET'])
def pohling():
    pass

@app.route('/api/getIndoorEnv', method=['GET'])
def getIndoorEnv():
    pass

@app.route('/api/command', method=['POST'])
def command():
    pass
