# -*- coding: utf-8 -*-
#import pprint
import logging
from imapclient import IMAPClient



def clear_outbox(server, login, password, folder, test_name, log_file):
    """
    Clear the SENT folder before sending emails
    """
    try:
        logging.basicConfig(filename=log_file, level=logging.INFO)
        logging.info("%s. Clearing Outbox -- Start" % test_name)
        with IMAPClient(server) as client:
            client.login(login, password)
            #  get names of the mailbox folders
            #pprint.pprint(client.list_folders())  
            client.select_folder(folder, readonly=False)
            client.delete_messages(client.search(['ALL']))
            client.expunge()
        logging.info("%s. Clearing Outbox -- OK" % test_name)
    except:
        logging.error("%s. Clearing Outbox -- ERROR" % test_name)

        

def read_outbox(server, login, password, folder, test_name, log_file):
    """
    Get an amount of sent messages to make sure 
    that emails were sent correctly
    """
    try:
        logging.basicConfig(filename=log_file, level=logging.INFO)
        logging.info("%s. Reading Outbox -- Start" % test_name)
        with IMAPClient(server) as client:
            client.login(login, password)
            #  Select the SENT folder
            client.select_folder(folder, readonly=False)
            #  Select ALL messages
            sent_messages = client.search(['ALL'])

        actual_result = len(sent_messages)

        logging.info('%s. Sent emails: %s' % (test_name, actual_result))
    except:
        logging.error("%s. Reading Outbox -- ERROR" % test_name)


if __name__ == "main":
    pass