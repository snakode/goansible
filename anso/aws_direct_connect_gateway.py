import random
import string
import os
from register import registerObj
import writer

class aws_direct_connect_gateway:
    playbook_name = ''
    hosts=[]
    register=[]
    amazon_asn = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    direct_connect_gateway_id = ''
    ec2_url = ''
    name = ''
    profile = ''
    region = ''
    security_token = ''
    state = ''
    validate_certs = ''
    virtual_gateway_id = ''
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

