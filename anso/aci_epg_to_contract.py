import random
import string
import os
from register import registerObj
import writer

class aci_epg_to_contract:
    playbook_name = ''
    hosts=[]
    register=[]
    contract_type = ''
    host = ''
    password = ''
    private_key = ''
    ap = ''
    certificate_name = ''
    contract = ''
    epg = ''
    output_level = ''
    port = ''
    priority = ''
    provider_match = ''
    state = ''
    tenant = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
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

