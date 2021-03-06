import random
import string
import os
from register import registerObj
import writer

class fmgr_device_provision_template:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    device_unique_name = ''
    provision_targets = ''
    provisioning_template = ''
    admin_enable_fortiguard = ''
    admin_fortianalyzer_target = ''
    admin_fortiguard_target = ''
    admin_gui_theme = ''
    admin_http_port = ''
    admin_https_port = ''
    admin_https_redirect = ''
    admin_language = ''
    admin_switch_controller = ''
    admin_timeout = ''
    delete_provisioning_template = ''
    dns_primary_ipv4 = ''
    dns_secondary_ipv4 = ''
    dns_suffix = ''
    mode = ''
    ntp_auth = ''
    ntp_auth_pwd = ''
    ntp_server = ''
    ntp_status = ''
    ntp_sync_interval = ''
    ntp_type = ''
    ntp_v3 = ''
    smtp_conn_sec = ''
    smtp_password = ''
    smtp_port = ''
    smtp_replyto = ''
    smtp_server = ''
    smtp_source_ipv4 = ''
    smtp_username = ''
    smtp_validate_cert = ''
    snmp_status = ''
    snmp_v2c_id = ''
    snmp_v2c_name = ''
    snmp_v2c_query_hosts_ipv4 = ''
    snmp_v2c_query_port = ''
    snmp_v2c_query_status = ''
    snmp_v2c_status = ''
    snmp_v2c_trap_hosts_ipv4 = ''
    snmp_v2c_trap_port = ''
    snmp_v2c_trap_src_ipv4 = ''
    snmp_v2c_trap_status = ''
    snmpv3_auth_proto = ''
    snmpv3_auth_pwd = ''
    snmpv3_name = ''
    snmpv3_notify_hosts = ''
    snmpv3_priv_proto = ''
    snmpv3_priv_pwd = ''
    snmpv3_queries = ''
    snmpv3_query_port = ''
    snmpv3_security_level = ''
    snmpv3_source_ip = ''
    snmpv3_status = ''
    snmpv3_trap_rport = ''
    snmpv3_trap_status = ''
    syslog_certificate = ''
    syslog_enc_algorithm = ''
    syslog_facility = ''
    syslog_filter = ''
    syslog_mode = ''
    syslog_port = ''
    syslog_server = ''
    syslog_status = ''
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

