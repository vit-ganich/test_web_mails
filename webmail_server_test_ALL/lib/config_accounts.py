"""
Credentials for webmail accounts.
Some webmail requires permissions for 
third-party apps (like Python) to sign in 
(Rambler, Yahoo, etc). You need to allow 
access to the mailbox for other mail clients.
"""
class Defaults:

    log_file = r"C:\Sikuli\log_DEBUG.txt"
    database_path = r"C:\ProgramData\Falcongaze SecureTower\Databases\NewDatabase.db"
    number_of_sent_emails = 3
    query_to_db = "SELECT httpsess_mail_id FROM httpsess_mail WHERE httpsess_mail_subject = 'autotest'"


class Gmail:

    test_name = " 'Web-mail Gmail'"
    server = "imap.gmail.com"
    login = "***********"
    password = "***********"
    folder = "[Gmail]/Отправленные"
    #  path to cmd-file, which performs a remote launch of a script at the agent side
    cmd_starter_agent = r".\cmd_files\webmail_gmail.cmd"


class Yandex:

    test_name = " 'Web-mail Yandex'"
    server = "imap.yandex.ru"
    login = "********"
    password = "*******"
    folder = "Отправленные"
    #  path to cmd-file, which performs a remote launch of a script at the agent side
    cmd_starter_agent = r".\cmd_files\webmail_yandex.cmd"


class Mail_ru:

    test_name = " 'Web-mail Mail.ru'"
    server = "imap.mail.ru"
    login = "********@mail.ru"
    password = "********"
    folder = "Отправленные"
    #  path to cmd-file, which performs a remote launch of a script at the agent side
    cmd_starter_agent = r".\cmd_files\webmail_mail_ru.cmd"


class Rambler:

    test_name = " 'Web-mail Rambler'"
    server = "imap.rambler.ru"
    login = "*********"
    password = "*********"
    folder = "SentBox"
    #  path to cmd-file, which performs a remote launch of a script at the agent side
    cmd_starter_agent = r".\cmd_files\webmail_rambler.cmd"


class Yahoo:

    test_name = " 'Web-mail Yahoo'"
    server = "imap.mail.yahoo.com"
    login = "********"
    password = "************"
    folder = "Sent"
    #  path to cmd-file, which performs a remote launch of a script at the agent side
    cmd_starter_agent = r".\cmd_files\webmail_yahoo.cmd"


class Outlook:

    test_name = " 'Web-mail Outlook.com'"
    server = "imap-mail.outlook.com"
    login = "*******@outlook.com"
    password = "**********"
    folder = "Sent"
    #  path to cmd-file, which performs a remote launch of a script at the agent side
    cmd_starter_agent = r".\cmd_files\webmail_outlook.cmd"


class OWA:

    test_name = " 'Web-mail OWA'"
    server = "imap.corp.profigroup.by"
    login = "***********"
    password = "*******"
    folder = "INBOX"
    #  path to cmd-file, which performs a remote launch of a script at the agent side
    cmd_starter_agent = r".\cmd_files\webmail_owa.cmd"


if __name__ == "main":
    pass