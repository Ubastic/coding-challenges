from collections import OrderedDict


class Dinglemouse(object):

    def __init__(self):
        self.data = OrderedDict()

    def setAge(self, age):
        self.data['age'] = f'I am {age}.'
        return self

    def setSex(self, sex):
        self.data['sex'] = f'I am {"male" if sex == "M" else "female"}.'
        return self

    def setName(self, name):
        self.data['name'] = f'My name is {name}.'
        return self

    def hello(self):
        return ' '.join(['Hello.', *self.data.values()])