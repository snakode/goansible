import random
import string
import os
from register import registerObj
import writer

class netscaler_lb_vserver:
    playbook_name = ''
    hosts=[]
    register=[]
    nitro_pass = ''
    nitro_user = ''
    nsip = ''
    appflowlog = ''
    authentication = ''
    authenticationhost = ''
    authn401 = ''
    authnprofile = ''
    authnvsname = ''
    backuplbmethod = ''
    backuppersistencetimeout = ''
    bypassaaaa = ''
    cacheable = ''
    clttimeout = ''
    comment = ''
    connfailover = ''
    cookiename = ''
    datalength = ''
    dataoffset = ''
    dbprofilename = ''
    dbslb = ''
    disabled = ''
    disableprimaryondown = ''
    dns64 = ''
    dnsprofilename = ''
    downstateflush = ''
    hashlength = ''
    healththreshold = ''
    httpprofilename = ''
    icmpvsrresponse = ''
    insertvserveripport = ''
    ipmask = ''
    ippattern = ''
    ipv46 = ''
    l2conn = ''
    lbmethod = ''
    listenpolicy = ''
    listenpriority = ''
    m = ''
    macmoderetainvlan = ''
    maxautoscalemembers = ''
    minautoscalemembers = ''
    mssqlserverversion = ''
    mysqlcharacterset = ''
    mysqlprotocolversion = ''
    mysqlservercapabilities = ''
    mysqlserverversion = ''
    name = ''
    netmask = ''
    netprofile = ''
    newservicerequest = ''
    newservicerequestincrementinterval = ''
    newservicerequestunit = ''
    nitro_protocol = ''
    nitro_timeout = ''
    oracleserverversion = ''
    persistavpno = ''
    persistencebackup = ''
    persistencetype = ''
    persistmask = ''
    port = ''
    processlocal = ''
    push = ''
    pushlabel = ''
    pushmulticlients = ''
    pushvserver = ''
    range = ''
    recursionavailable = ''
    redirectportrewrite = ''
    redirurl = ''
    resrule = ''
    rhistate = ''
    rtspnat = ''
    save_config = ''
    servicebindings = ''
    servicegroupbindings = ''
    servicetype = ''
    sessionless = ''
    skippersistency = ''
    sobackupaction = ''
    somethod = ''
    sopersistence = ''
    sopersistencetimeout = ''
    sothreshold = ''
    ssl_certkey = ''
    state = ''
    tcpprofilename = ''
    td = ''
    timeout = ''
    tosid = ''
    v6netmasklen = ''
    v6persistmasklen = ''
    validate_certs = ''
    vipheader = ''
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

