import random
import string
import os
from register import registerObj
import writer

class vmware_guest:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    annotation = ''
    cdrom = ''
    cluster = ''
    convert = ''
    customization = ''
    customization_spec = ''
    customvalues = ''
    datacenter = ''
    datastore = ''
    disk = ''
    esxi_hostname = ''
    folder = ''
    force = ''
    guest_id = ''
    hardware = ''
    hostname = ''
    is_template = ''
    linked_clone = ''
    name_match = ''
    networks = ''
    password = ''
    port = ''
    resource_pool = ''
    snapshot_src = ''
    state = ''
    state_change_timeout = ''
    template = ''
    use_instance_uuid = ''
    username = ''
    uuid = ''
    validate_certs = ''
    vapp_properties = ''
    wait_for_customization = ''
    wait_for_ip_address = ''
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

