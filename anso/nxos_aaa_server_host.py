import random
import string
import os
from register import registerObj
import writer

class nxos_aaa_server_host:
    playbook_name = ''
    hosts=[]
    register=[]
    address = ''
    server_type = ''
    acct_port = ''
    auth_port = ''
    encrypt_type = ''
    host_timeout = ''
    key = ''
    provider = ''
    state = ''
    tacacs_port = ''
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

