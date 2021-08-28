from flask import Flask, request, Response, make_response
import sqlite3
import os
import model
import sql



INDOORENV_ID = 0
COMMAND_ID = 0

sql_hadller = sql.SqlHandler()

app = Flask(__name__)

@app.errorhandler(500)
def error_500(error):
    return 500

@app.route('/api/pohling', methods=['GET'])
def pohling():
    indoor_env = model.IndoorEnv()
    indoor_env.set_data_from_json(request.json)
    INDOORENV_ID =sql_hadller.insert_indoorEnv_column(indoor_env)

    command = model.AirConCommnad()
    if !COMMAND_ID < sql_handler.get_latest_command():
        return command.export_json(False)
    else:
        return command.export_json(True)
        

@app.route('/api/getIndoorEnv', methods=['GET'])
def getIndoorEnv():
    indoor_env = model.IndoorEnv()
    indoor_env.set_data_from_sql(sql_hadller.get_latest_indoorEnv())

    return indoor_env.export_json()

@app.route('/api/command', methods=['POST'])
def command():
    command = model.AirConCommnad()
    command.set_data_from_json(request.json)
    COMMAND_ID = sql_hadllerl.insert_command_column(command)

    sql_handler.insert_command(command)
    
    return "accept"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
