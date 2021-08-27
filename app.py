from flask import Flask, request, Response, make_response
import sqlite3
import os
from .model import indoorenvironment
from .model import airconcommand
from .service import sql

INDOORENV_ID = 0
COMMAND_ID = 0


app = Flask(__name__)

@app.errorhandler(500)
def error_500(error):
    return 500

@app.route('/api/pohling', methods=['GET'])
def pohling(sql_hadller):
    indoor_env = indoorenvironment.IndoorEnv()
    indoor_env.set_data_from_json(request.json)
    INDOORENV_ID =sql_hadller.insert_indoorEnv_column(indoor_env)

    command = airconcommand.AirConCommnad()

    
    return command.export_json()

@app.route('/api/getIndoorEnv', methods=['GET'])
def getIndoorEnv(sql_hadller):
    indoor_env = indoorenvironment.IndoorEnv()
    indoor_env.set_data_from_sql(sql_hadller.get_latest_indoorEnv())

    return indoor_env.export_json

@app.route('/api/command', methods=['POST'])
def command(sql_hadller):
    command = airconcommand.AirConCommnad()
    command.set_data_from_json(request.json)
    COMMAND_ID = sq_hadllerl.insert_command_column(command)

    sql.insert_command(command)
    
    return "accept"

if __name__ == '__main__':
    sql_hadller = sql.SqlHandler()
    main(sql_hadller)
