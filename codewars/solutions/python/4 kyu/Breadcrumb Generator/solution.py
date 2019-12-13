from urlparse import urlparse

IGNORE = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]


def _process_part(s):
    a = s.split('-')
    return s.replace('-', ' ').upper() if len(s) < 30 else ''.join(c[0].upper() for c in a if c not in IGNORE)


def generate_bc(url, separator):
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split('/')[1:] if p]
    if parts and parts[-1].startswith('index.'):
        parts = parts[:-1]
    parts = [p.split('.')[0] for p in parts]

    if parts:
        results = ['<a href="/">HOME</a>']
    else:
        results = ['<span class="active">HOME</span>']

    for i, p in enumerate(parts[:-1]):
        results.append('<a href="/{}/">{}</a>'.format('/'.join(parts[:i + 1]), _process_part(p)))
    if parts:
        results.append('<span class="active">{}</span>'.format(_process_part(parts[-1])))

    return separator.join(results)