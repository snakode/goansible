import random
import string
import os
from register import registerObj
import writer

class execute_lambda:
    playbook_name = ''
    hosts=[]
    register=[]
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    dry_run = ''
    ec2_url = ''
    function_arn = ''
    name = ''
    payload = ''
    profile = ''
    region = ''
    security_token = ''
    tail_log = ''
    validate_certs = ''
    version_qualifier = ''
    wait = ''
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

