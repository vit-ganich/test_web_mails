class General():

	#  Credentials for all accounts
	login = r"fgqa.autotest"
	password = r"23072307au"

	#  Login for Oulook.com
	login_outlook = "fgqa.autotest@outlook.com"
	
	#  Credentials for Oulook Web Access
	login_owa = "pg/stqatester01"
	password_owa = "c@#DvTuu"

	address_to = r"ganich.test@yandex.ru"
	log_file = r"C:\Sikuli\DEBUG_log.txt"


class Gmail():

	test_name = "Webmail_Gmail"
	startpage = "https://mail.google.com/"
	#  selectors
	login_field = "//*[@name='identifier']"
	password_field = "//*[@name='password']"
	compose_button = "//div[@class='aic']/div/div"
	address_to_field = "//*[@name='to']"
	subject_field = "//*[@name='subjectbox']"


class Mail_ru():

	test_name = "Webmail_Mail_ru"
	#  selectors
	startpage = "https://www.mail.ru/"
	login_field = "//*[@id='mailbox:login']"
	password_field = "//*[@id='mailbox:password']"
	compose_button = "//*[@data-name='compose']/span"
	address_to_field = "//*[@data-original-name='To']"
	subject_field = "//*[@name='Subject']"


class OWA():

	test_name = "Web_mail_OWA"
	
	startpage = r"https://pg-m.pg.local/owa/auth/logon.aspx?url=https://pg-m.pg.local/owa/&reason=0"
	#  selectors
	login_field = "//*[@id='username']"
	password_field = "//*[@id='password']"
	compose_button = "//*[@id='lnkHdrnewmsg']"
	address_to_field = "//*[@id='txtto']"
	subject_field = "//*[@id='txtsbj']"
	mailbody_field = "//*[@name='txtbdy']"
	send_button = "//*[@id ='lnkHdrsend']"


class Rambler():

	test_name = "Web_mail_Rambler"
	startpage = "https://mail.rambler.ru/"
	#  selectors
	login_field = "//*[@name='login']"
	password_field = "//*[@name='password']"
	compose_button = "//*[@href='#/compose']/span"
	address_to_field = "//*[@id='receivers']"
	subject_field = "//*[@id='subject']"
	send_button = "//*[@data-compose-button='bottom']"


class Yahoo():

	test_name = "Web_mail_Yahoo"
	startpage = "https://mail.yahoo.com/"
	#  selectors
	login_field = "//*[@id='login-username']"
	password_field = "//*[@id='login-passwd']"
	compose_button = "//*[@aria-label='Compose']"
	address_to_field = "//*[@id='message-to-field']"
	subject_field = "//*[@placeholder='Subject']"
	mailbody_field = "//*[@role='textbox']"
	send_button = "(//button[@type='button'])[6]"


class Yandex():

	test_name = "Web_mail_Yandex"
	startpage = "https://mail.yandex.ru/"
	#  selectors
	login_button = "//*[@data-reactid='24']"
	login_field = "//*[@name='login']"
	password_field = "//*[@name='passwd']"
	compose_button = "//*[@href='#compose']"
	address_to_field = "//*[@name='to']"
	subject_field = "//input[contains(@name,'subj')]"


class Outlook():

	test_name = "Web_mail_Outlook-beta"
	startpage = "https://outlook.live.com/owa/"
	#  selectors
	login_button = "//*[@class='buttonLargeBlue']"
	login_field = "//*[@name='loginfmt']"
	password_field = "//*[@name='passwd']"
	compose_button = "//div[@class='E3gtdMNeYEe-Iir2VeZLC']/button"
	password_field = "//*[@name='passwd']"
	subject_field = "//input[starts-with(@id,'subjectLine')]"