import random
import string
import os
from register import registerObj
import writer

class zabbix_hostmacro:
    playbook_name = ''
    hosts=[]
    register=[]
    host_name = ''
    http_login_user = ''
    login_password = ''
    login_user = ''
    macro_name = ''
    macro_value = ''
    server_url = ''
    force = ''
    http_login_password = ''
    state = ''
    timeout = ''
    validate_certs = ''
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

