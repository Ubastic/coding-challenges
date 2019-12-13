def DNA_strand(dna):
    d = {'C': 'G', 'G': 'C', 'A': 'T', 'T': 'A'}
    return ''.join(d.get(s, s) for s in dna)
