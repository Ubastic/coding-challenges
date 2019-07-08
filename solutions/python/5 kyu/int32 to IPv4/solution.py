def int32_to_ip(int32):
    return '.'.join([f'{int32 // (256 ** i) % 256}' for i in range(4)][::-1])
