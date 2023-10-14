import logging
import azure.functions as func

import pyodbc
server = 'inviewdb.database.windows.net'
database = 'stockforecast'
username = 'schleidt'
password = 'Internet1231'
driver= '{ODBC Driver 17 for SQL Server}'


app = func.FunctionApp()

@app.schedule(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger_savestockclosing(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    # connect to db and 'write a aline'
    """ with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT TOP 3 * FROM dbo.Results")
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[1]))
                row = cursor.fetchone() """

    logging.info('Python timer trigger function executed.')