def ip_to_int32(ip):
    return int(''.join(bin(int(i))[2:].zfill(8) for i in ip.split('.')), 2)
