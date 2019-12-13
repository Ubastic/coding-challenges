class SecureList():
    def __init__(self, lst):
        self.data = list(lst)
    
    def __repr__(self):
        d, self.data = self.data, []
        return repr(d)
        
    def __str__(self):
        return repr(self)
    
    def __getattr__(self, item):
        return getattr(self.data, item)
    
    def __getitem__(self, item):
        return self.data.pop(item)
  