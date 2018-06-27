#module forwarding.py
#coming from p4tutorials
def addForwarding(p4info_helper, sw,
                     dst_eth_addr, dst_ip_addr, port):
    """
    :param p4info_helper: the P4Info helper
    :param ingress_sw: the ingress switch connection
    :param egress_sw: the egress switch connection
    :param dst_ip_addr: the destination IP to match in the ingress rule
    :param dst_eth_addr: the destination Ethernet address to write in the
                        egress rule
    """
    table_entry = p4info_helper.buildTableEntry(
        table_name="MyIngress.ipv4_lpm",
        match_fields={
            "hdr.ipv4.dstAddr": (dst_ip_addr, 32)
        },
        action_name="MyIngress.ipv4_forward",
        action_params={
            "dstAddr": dst_eth_addr,
            "port": port
        })
    sw.WriteTableEntry(table_entry, dry_run=True)
    print "Installed fwd rule on %s" % sw.name

def rmForwarding(p4info_helper, sw, dst_eth_addr, dst_ip_addr, port):
    table_entry = p4info_helper.buildTableEntry(
        table_name="MyIngress.ipv4_lpm",
        match_fields={
            "hdr.ipv4.dstAddr": (dst_ip_addr, 32)
        },
        action_name="MyIngress.drop()")
    sw.WriteTableEntry(table_entry, dry_run=True)
    print "Installed fwd rule on %s" % sw.name
