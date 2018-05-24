# -*- coding: utf-8 -*-
from config_folder import base_class as base
from config_folder.config import General as gen
from config_folder.config import Outlook as conf


try:
    Start = base.BaseClass(conf.test_name, gen.login_outlook, gen.password, gen.address_to, gen.log_file)
    Start.set_up(conf.startpage, sleep=5)
    Start.press_button(conf.login_button, sleep=5)
    Start.enter_login(conf.login_field, sleep=3, with_enter=True)
    Start.enter_password(conf.password_field, sleep=7, with_enter=True)
    for item in range (1,4):
        Start.press_button(conf.compose_button, sleep=3)
        Start.enter_address_to(sleep=1)
        Start.enter_subject(conf.subject_field, sleep=1)
        Start.enter_mail_body(item, conf.subject_field, sleep=1, with_tab=True)
        Start.press_ctrl_enter(sleep=2)
except:
    Start.write_log("finished with ERROR")
finally:
    Start.tear_down(sleep=3)
    Start.write_log("finished succesfully" )