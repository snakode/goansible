import random
import string
import os
from register import registerObj
import writer

class ucs_vhba_template:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    name = ''
    password = ''
    description = ''
    fabric = ''
    max_data = ''
    org_dn = ''
    pin_group = ''
    port = ''
    proxy = ''
    qos_policy = ''
    redundancy_type = ''
    state = ''
    stats_policy = ''
    template_type = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
    vsan = ''
    wwpn_pool = ''
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

