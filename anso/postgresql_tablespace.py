import random
import string
import os
from register import registerObj
import writer

class postgresql_tablespace:
    playbook_name = ''
    hosts=[]
    register=[]
    tablespace = ''
    ca_cert = ''
    db = ''
    location = ''
    login_host = ''
    login_password = ''
    login_unix_socket = ''
    login_user = ''
    owner = ''
    port = ''
    rename_to = ''
    session_role = ''
    set = ''
    ssl_mode = ''
    state = ''
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

