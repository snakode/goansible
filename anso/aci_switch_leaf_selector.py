import random
import string
import os
from register import registerObj
import writer

class aci_switch_leaf_selector:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    certificate_name = ''
    description = ''
    from = ''
    leaf = ''
    leaf_node_blk = ''
    leaf_node_blk_description = ''
    leaf_profile = ''
    output_level = ''
    policy_group = ''
    port = ''
    state = ''
    timeout = ''
    to = ''
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

