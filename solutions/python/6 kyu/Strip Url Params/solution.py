from collections import OrderedDict


def strip_url_params(url, params_to_strip=[]):
    if '?' not in url:
        return url
    
    values = OrderedDict()
    base, additional = url.split('?', 1)
    for part in additional.split('&'):
        name, value = part.split('=')
        if name not in values and name not in params_to_strip:
            values[name] = value

    return '{}?{}'.format(base, '&'.join('{}={}'.format(key, value) for key, value in values.items()))
    