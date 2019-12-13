def ip_value(ip):
    return sum(int(a) << (24 - i * 8) for i, a in enumerate(ip.split('.')))


def ips_between(start, end):
    return ip_value(end) - ip_value(start)
