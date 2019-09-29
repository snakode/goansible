import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_voip:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    comment = ''
    mode = ''
    name = ''
    sccp = ''
    sccp_block_mcast = ''
    sccp_log_call_summary = ''
    sccp_log_violations = ''
    sccp_max_calls = ''
    sccp_status = ''
    sccp_verify_header = ''
    sip = ''
    sip_ack_rate = ''
    sip_block_ack = ''
    sip_block_bye = ''
    sip_block_cancel = ''
    sip_block_geo_red_options = ''
    sip_block_info = ''
    sip_block_invite = ''
    sip_block_long_lines = ''
    sip_block_message = ''
    sip_block_notify = ''
    sip_block_options = ''
    sip_block_prack = ''
    sip_block_publish = ''
    sip_block_refer = ''
    sip_block_register = ''
    sip_block_subscribe = ''
    sip_block_unknown = ''
    sip_block_update = ''
    sip_bye_rate = ''
    sip_call_keepalive = ''
    sip_cancel_rate = ''
    sip_contact_fixup = ''
    sip_hnt_restrict_source_ip = ''
    sip_hosted_nat_traversal = ''
    sip_info_rate = ''
    sip_invite_rate = ''
    sip_ips_rtp = ''
    sip_log_call_summary = ''
    sip_log_violations = ''
    sip_malformed_header_allow = ''
    sip_malformed_header_call_id = ''
    sip_malformed_header_contact = ''
    sip_malformed_header_content_length = ''
    sip_malformed_header_content_type = ''
    sip_malformed_header_cseq = ''
    sip_malformed_header_expires = ''
    sip_malformed_header_from = ''
    sip_malformed_header_max_forwards = ''
    sip_malformed_header_p_asserted_identity = ''
    sip_malformed_header_rack = ''
    sip_malformed_header_record_route = ''
    sip_malformed_header_route = ''
    sip_malformed_header_rseq = ''
    sip_malformed_header_sdp_a = ''
    sip_malformed_header_sdp_b = ''
    sip_malformed_header_sdp_c = ''
    sip_malformed_header_sdp_i = ''
    sip_malformed_header_sdp_k = ''
    sip_malformed_header_sdp_m = ''
    sip_malformed_header_sdp_o = ''
    sip_malformed_header_sdp_r = ''
    sip_malformed_header_sdp_s = ''
    sip_malformed_header_sdp_t = ''
    sip_malformed_header_sdp_v = ''
    sip_malformed_header_sdp_z = ''
    sip_malformed_header_to = ''
    sip_malformed_header_via = ''
    sip_malformed_request_line = ''
    sip_max_body_length = ''
    sip_max_dialogs = ''
    sip_max_idle_dialogs = ''
    sip_max_line_length = ''
    sip_message_rate = ''
    sip_nat_trace = ''
    sip_no_sdp_fixup = ''
    sip_notify_rate = ''
    sip_open_contact_pinhole = ''
    sip_open_record_route_pinhole = ''
    sip_open_register_pinhole = ''
    sip_open_via_pinhole = ''
    sip_options_rate = ''
    sip_prack_rate = ''
    sip_preserve_override = ''
    sip_provisional_invite_expiry_time = ''
    sip_publish_rate = ''
    sip_refer_rate = ''
    sip_register_contact_trace = ''
    sip_register_rate = ''
    sip_rfc2543_branch = ''
    sip_rtp = ''
    sip_ssl_algorithm = ''
    sip_ssl_auth_client = ''
    sip_ssl_auth_server = ''
    sip_ssl_client_certificate = ''
    sip_ssl_client_renegotiation = ''
    sip_ssl_max_version = ''
    sip_ssl_min_version = ''
    sip_ssl_mode = ''
    sip_ssl_pfs = ''
    sip_ssl_send_empty_frags = ''
    sip_ssl_server_certificate = ''
    sip_status = ''
    sip_strict_register = ''
    sip_subscribe_rate = ''
    sip_unknown_header = ''
    sip_update_rate = ''
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
