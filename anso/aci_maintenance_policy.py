import random
import string
import os
from register import registerObj
import writer

class aci_maintenance_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    name = ''
    password = ''
    private_key = ''
    scheduler = ''
    adminst = ''
    certificate_name = ''
    graceful = ''
    ignoreCompat = ''
    output_level = ''
    port = ''
    runmode = ''
    state = ''
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

