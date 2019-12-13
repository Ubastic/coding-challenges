create_class = lambda name, inheritance=(object,), methods=(): type(name, inheritance, {method.__name__: method for method in methods})
