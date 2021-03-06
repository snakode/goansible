import random
import string
import os
from register import registerObj
import writer

class cs_portforward:
    playbook_name = ''
    hosts=[]
    register=[]
    ip_address = ''
    private_port = ''
    public_port = ''
    account = ''
    api_http_method = ''
    api_key = ''
    api_region = ''
    api_secret = ''
    api_timeout = ''
    api_url = ''
    domain = ''
    network = ''
    open_firewall = ''
    poll_async = ''
    private_end_port = ''
    project = ''
    protocol = ''
    public_end_port = ''
    state = ''
    tags = ''
    vm = ''
    vm_guest_ip = ''
    vpc = ''
    zone = ''
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

