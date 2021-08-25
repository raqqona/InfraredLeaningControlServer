from flask import Flask, request, Response, make_response
import sqlite3
import os
from model import airconcommand
from model import indoorenvironment

app = Flask(__name__)

@app.errorhandler(500)
def error_500(error):
    return 500

@app.route('/api/pohling', methods=['GET'])
def pohling():
    indoor_env = indoorenvironment.IndoorEnv()
    indoor_env.set_data_from_json(request.json)

    command = airconcommand.AirConCommnad()

    command_json = get_command()
    
    return command_json

@app.route('/api/getIndoorEnv', methods=['GET'])
def getIndoorEnv():
    indoor_env = indoorenvironment.IndoorEnv()
    indoor_env.set_data_from_sql(get_indoorenv())

    return indoorEnv_json

@app.route('/api/command', methods=['POST'])
def command():
    command = airconcommand.AirConCommnad()
    command.set_data_from_json(request.json)

    insert_command(command)
    
    return "accept"
