from common.methods import set_progress, is_ip_pingable


def run(job, logger=None, **kwargs):
    """
    Pings the IP address associated with the NIC passed.
    """
    nic = kwargs.get("nic")
    svr = nic.server
    if svr.c2_skip_network_conf:
        set_progress(
            "Skipping ping test since network configuration was skipped")
        return "", "", ""
    pingable = is_ip_pingable(nic.ip)
    if pingable:
        set_progress("Successfully pinged {}".format(nic.ip))
        return "", "", ""
    else:
        set_progress("Failed to ping {}".format(nic.ip))
        return "FAILURE", "Failed to ping {}".format(nic.ip), ""
