import random
import string
import os
from register import registerObj
import writer

class mysql_user:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    append_privs = ''
    ca_cert = ''
    check_implicit_admin = ''
    client_cert = ''
    client_key = ''
    config_file = ''
    connect_timeout = ''
    encrypted = ''
    host = ''
    host_all = ''
    login_host = ''
    login_password = ''
    login_port = ''
    login_unix_socket = ''
    login_user = ''
    password = ''
    priv = ''
    sql_log_bin = ''
    state = ''
    update_password = ''
    def compile(self):
       self.playbook_name=writer.writer(self,self.playbook_name)

    def run(self):
       dump_name=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
       os.system('{} | tee {}'.format(self.playbook_name,dump_name))
       self.register = registerObj(dump_name)
       os.remove(dump_name)

    def go(self):
       self.compile()
       self.run()

