import random
import string
import os
from register import registerObj
import writer

class na_ontap_user:
    playbook_name = ''
    hosts=[]
    register=[]
    applications = ''
    authentication_method = ''
    hostname = ''
    name = ''
    password = ''
    username = ''
    vserver = ''
    http_port = ''
    https = ''
    lock_user = ''
    ontapi = ''
    role_name = ''
    set_password = ''
    state = ''
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

