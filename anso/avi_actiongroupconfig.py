import random
import string
import os
from register import registerObj
import writer

class avi_actiongroupconfig:
    playbook_name = ''
    hosts=[]
    register=[]
    external_only = ''
    level = ''
    name = ''
    action_script_config_ref = ''
    api_context = ''
    api_version = ''
    autoscale_trigger_notification = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    description = ''
    email_config_ref = ''
    password = ''
    snmp_trap_profile_ref = ''
    state = ''
    syslog_config_ref = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    username = ''
    uuid = ''
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

