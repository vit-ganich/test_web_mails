import sqlite3          
import logging

"""
This script is common to all web-mails
"""

def connect(db_path, expected_result, test_name, log_file, query, result=[]):
    ex_code = 1
    #  foo returns answer "ex_code" 0 - success, 1 - error, 2 - success, but attention required
    try:
        logging.basicConfig(filename=log_file, level=logging.INFO)
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        #  get tte list of sent emails
        cursor.execute(query)
        actual_result = cursor.fetchall()
        logging.info("%s. Intercepted emails: %s" % (test_name, len(actual_result)))
        #  if the number of intercepted emails in DB >= number of sent emails - Test Passed! 
        if len(actual_result) == expected_result:
            return 'Успешно пройден'
        elif len(actual_result) != expected_result and len(actual_result) > 0:
            return 'Успешно пройден (!)'
        else:
            return 'Ошибка в тесте'
    except:
        logging.error(" %s -- Database connection -- ERROR" % test_name)
        return 'Ошибка подключения к БД'
        

if __name__ == "main":
    pass