# -*- coding: utf-8 -*-
from config_folder import base_class as base
from config_folder.config import General as gen
from config_folder.config import Yahoo as conf


try:
    Start = base.BaseClass(conf.test_name, gen.login, gen.password, gen.address_to, gen.log_file)
    Start.set_up(conf.startpage, sleep=10)
    Start.enter_login(conf.login_field, sleep=5, with_enter=True)
    Start.enter_password(conf.password_field, sleep=10, with_enter=True)
    for item in range (1,4):
        Start.press_compose_button(conf.compose_button, sleep=1)
        Start.enter_address_to(conf.address_to_field, sleep=1)
        Start.enter_subject(conf.subject_field, sleep=1)
        Start.enter_mail_body(item, conf.mailbody_field, sleep=1)
        Start.press_send_button(conf.send_button, sleep=2)
except:
    Start.write_log("finished with ERROR")
finally:
    Start.tear_down(sleep=2)
    Start.write_log("finished succesfully" )