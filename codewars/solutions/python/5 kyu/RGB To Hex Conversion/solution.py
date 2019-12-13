def rgb(r, g, b):
    return ''.join('{:02X}'.format(((i if i < 256 else 255) if i > 0 else 0)) for i in (r, g, b))
