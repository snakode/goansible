import random
import string
import os
from register import registerObj
import writer

class udm_user:
    playbook_name = ''
    hosts=[]
    register=[]
    username = ''
    birthday = ''
    city = ''
    country = ''
    department_number = ''
    description = ''
    display_name = ''
    email = ''
    employee_number = ''
    employee_type = ''
    firstname = ''
    gecos = ''
    groups = ''
    home_share = ''
    home_share_path = ''
    home_telephone_number = ''
    homedrive = ''
    lastname = ''
    mail_alternative_address = ''
    mail_home_server = ''
    mail_primary_address = ''
    mobile_telephone_number = ''
    organisation = ''
    ou = ''
    override_pw_history = ''
    override_pw_length = ''
    pager_telephonenumber = ''
    password = ''
    phone = ''
    position = ''
    postcode = ''
    primary_group = ''
    profilepath = ''
    pwd_change_next_login = ''
    room_number = ''
    samba_privileges = ''
    samba_user_workstations = ''
    sambahome = ''
    scriptpath = ''
    secretary = ''
    serviceprovider = ''
    shell = ''
    state = ''
    street = ''
    subpath = ''
    title = ''
    unixhome = ''
    update_password = ''
    userexpiry = ''
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

