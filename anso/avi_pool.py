import random
import string
import os
from register import registerObj
import writer

class avi_pool:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    a_pool = ''
    ab_pool = ''
    ab_priority = ''
    api_context = ''
    api_version = ''
    apic_epg_name = ''
    application_persistence_profile_ref = ''
    autoscale_launch_config_ref = ''
    autoscale_networks = ''
    autoscale_policy_ref = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    capacity_estimation = ''
    capacity_estimation_ttfb_thresh = ''
    cloud_config_cksum = ''
    cloud_ref = ''
    connection_ramp_duration = ''
    controller = ''
    created_by = ''
    default_server_port = ''
    description = ''
    domain_name = ''
    east_west = ''
    enabled = ''
    external_autoscale_groups = ''
    fail_action = ''
    fewest_tasks_feedback_delay = ''
    graceful_disable_timeout = ''
    gslb_sp_enabled = ''
    health_monitor_refs = ''
    host_check_enabled = ''
    inline_health_monitor = ''
    ipaddrgroup_ref = ''
    lb_algorithm = ''
    lb_algorithm_consistent_hash_hdr = ''
    lb_algorithm_core_nonaffinity = ''
    lb_algorithm_hash = ''
    lookup_server_by_name = ''
    max_concurrent_connections_per_server = ''
    max_conn_rate_per_server = ''
    networks = ''
    nsx_securitygroup = ''
    password = ''
    pki_profile_ref = ''
    placement_networks = ''
    prst_hdr_name = ''
    request_queue_depth = ''
    request_queue_enabled = ''
    rewrite_host_header_to_server_name = ''
    rewrite_host_header_to_sni = ''
    server_auto_scale = ''
    server_count = ''
    server_name = ''
    server_reselect = ''
    servers = ''
    sni_enabled = ''
    ssl_key_and_certificate_ref = ''
    ssl_profile_ref = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    use_service_port = ''
    username = ''
    uuid = ''
    vrf_ref = ''
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
