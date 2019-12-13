def domain_name(url):
    dom = url.split('//', 1)[-1].split('/')[0]
    return (dom.split('www.')[-1] if dom.startswith('www.') else dom).split('.')[0]
