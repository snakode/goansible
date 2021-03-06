import random
import string
import os
from register import registerObj
import writer

class avi_controllerproperties:
    playbook_name = ''
    hosts=[]
    register=[]
    allow_ip_forwarding = ''
    allow_unauthenticated_apis = ''
    allow_unauthenticated_nodes = ''
    api_context = ''
    api_idle_timeout = ''
    api_version = ''
    appviewx_compat_mode = ''
    attach_ip_retry_interval = ''
    attach_ip_retry_limit = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    bm_use_ansible = ''
    cluster_ip_gratuitous_arp_period = ''
    controller = ''
    crashed_se_reboot = ''
    dead_se_detection_timer = ''
    dns_refresh_period = ''
    dummy = ''
    enable_memory_balancer = ''
    fatal_error_lease_time = ''
    max_dead_se_in_grp = ''
    max_pcap_per_tenant = ''
    max_seq_attach_ip_failures = ''
    max_seq_vnic_failures = ''
    password = ''
    persistence_key_rotate_period = ''
    portal_token = ''
    query_host_fail = ''
    safenet_hsm_version = ''
    se_create_timeout = ''
    se_failover_attempt_interval = ''
    se_offline_del = ''
    se_vnic_cooldown = ''
    secure_channel_cleanup_timeout = ''
    secure_channel_controller_token_timeout = ''
    secure_channel_se_token_timeout = ''
    seupgrade_fabric_pool_size = ''
    seupgrade_segroup_min_dead_timeout = ''
    ssl_certificate_expiry_warning_days = ''
    state = ''
    tenant = ''
    tenant_uuid = ''
    unresponsive_se_reboot = ''
    upgrade_dns_ttl = ''
    upgrade_lease_time = ''
    url = ''
    username = ''
    uuid = ''
    vnic_op_fail_time = ''
    vs_apic_scaleout_timeout = ''
    vs_awaiting_se_timeout = ''
    vs_key_rotate_period = ''
    vs_se_attach_ip_fail = ''
    vs_se_bootup_fail = ''
    vs_se_create_fail = ''
    vs_se_ping_fail = ''
    vs_se_vnic_fail = ''
    vs_se_vnic_ip_fail = ''
    warmstart_se_reconnect_wait_time = ''
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

