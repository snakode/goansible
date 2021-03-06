import random
import string
import os
from register import registerObj
import writer

class vultr_firewall_rule:
    playbook_name = ''
    hosts=[]
    register=[]
    group = ''
    api_account = ''
    api_endpoint = ''
    api_key = ''
    api_retries = ''
    api_timeout = ''
    cidr = ''
    end_port = ''
    ip_version = ''
    protocol = ''
    start_port = ''
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

