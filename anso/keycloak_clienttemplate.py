import random
import string
import os
from register import registerObj
import writer

class keycloak_clienttemplate:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_client_id = ''
    auth_keycloak_url = ''
    auth_password = ''
    auth_realm = ''
    auth_username = ''
    attributes = ''
    auth_client_secret = ''
    description = ''
    full_scope_allowed = ''
    id = ''
    name = ''
    protocol = ''
    protocol_mappers = ''
    realm = ''
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

