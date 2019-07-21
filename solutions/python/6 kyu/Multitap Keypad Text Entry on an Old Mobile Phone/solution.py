codes = [
        '1', 'abc2',  'def3', 
     'ghi4', 'jkl5',  'mno6', 
    'pqrs7', 'tuv8', 'wxyz9', 
        '*',   ' 0',     '#',
]

def presses(phrase):
    return sum(next((a.index(c) + 1 for a in codes if c in a), 0) for c in phrase.lower())