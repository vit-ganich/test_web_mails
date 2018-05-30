# -*- coding: utf-8 -*-
import subprocess
import os
import time
from lib import write_log as Log
from lib import imap_postman as Postman
from lib import database_connect as Database
from lib.config_accounts import Defaults
#  change only this line for different mail clients
from lib.config_accounts import Yandex as MailAccounts


test_name = MailAccounts.test_name
log_file = Defaults.log_file
cmd_file = MailAccounts.cmd_starter_agent  #  cmd to launch a script at the agent side

server = MailAccounts.server  #  for IMAP
login = MailAccounts.login  #  for IMAP
password = MailAccounts.password  #  for IMAP
folder = MailAccounts.folder  #  for IMAP
expected_result = Defaults.number_of_sent_emails  #  for database connection
db_path = Defaults.database_path  #  for database connection
query = Defaults.query_to_db  #  for database connection

  
try:
    #  Clear Outbox via IMAP before sending emails
    Postman.clear_outbox(server, login, password, folder, test_name, log_file)
    #  Run the script on the agent side for emails generation
    os.system(cmd_file)
    time.sleep(60)
    #  Get info about a number of sent emails
    Postman.read_outbox(server, login, password, folder, test_name, log_file)
    #  Connect to DB to compare the actual result with expected
    message = Database.connect(db_path, expected_result, test_name, log_file, query)
except:
    message = 'Неизвестная ошибка'
finally:
    Log.writeLog(test_name, message)