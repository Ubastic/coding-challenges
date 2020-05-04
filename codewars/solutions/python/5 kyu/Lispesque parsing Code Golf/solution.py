f=float
def parse(c, t):
	m=search(r'\([^(]*?\)', c)
	if not m:return f(c)
	g=m.group();n,*a=g[1:-1].split()
	return parse(c.replace(g,str(t[n](*map(f,a)))),t)