import random
import string
import os
from register import registerObj
import writer

class yum:
    playbook_name = ''
    hosts=[]
    register=[]
    allow_downgrade = ''
    autoremove = ''
    bugfix = ''
    conf_file = ''
    disable_excludes = ''
    disable_gpg_check = ''
    disable_plugin = ''
    disablerepo = ''
    download_dir = ''
    download_only = ''
    enable_plugin = ''
    enablerepo = ''
    exclude = ''
    install_weak_deps = ''
    installroot = ''
    list = ''
    lock_timeout = ''
    name = ''
    releasever = ''
    security = ''
    skip_broken = ''
    state = ''
    update_cache = ''
    update_only = ''
    use_backend = ''
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

