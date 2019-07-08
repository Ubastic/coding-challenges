import datetime
import re

EMAIL_REGEX = re.compile(r'\w{2,}(\.\w{2,})?@\w{2,}\.\w{2,}')


class ValidationError(Exception):
    def __init__(self, attribute_name, msg):
        self.attribute_name = attribute_name
        self.msg = msg

    def __str__(self):
        return 'Attribute `%s`: %s.' % (self.attribute_name, self.msg)


class Field(object):
    type = None

    def __init__(self, default=None, blank=False):
        self.default = default
        self.blank = blank

    def get_default(self):
        return self.default

    def validate(self, val):
        if not self.blank and val is None:
            return False
        elif not self.blank or (self.blank and val is not None):
            return isinstance(val, self.type) and self.sub_validation(val)
        return True

    def sub_validation(self, val):
        return True


class CharField(Field):
    type = str

    def __init__(self, min_length=0, max_length=None, default=None, blank=False):
        super(CharField, self).__init__(default, blank)
        self.max_length = max_length
        self.min_length = min_length

    def sub_validation(self, val):
        return not (self.min_length is not None and len(val) < self.min_length or
                    self.max_length is not None and len(val) > self.max_length)


class EmailField(CharField):
    def sub_validation(self, val):
        return EMAIL_REGEX.match(val) is not None


class IntegerField(Field):
    type = int

    def __init__(self, min_value=None, max_value=None, default=None, blank=False):
        super(IntegerField, self).__init__(default, blank)
        self.min_value = min_value
        self.max_value = max_value

    def sub_validation(self, val):
        return not (self.min_value is not None and val < self.min_value or
                    self.max_value is not None and val > self.max_value)


class BooleanField(Field):
    type = bool


class DateTimeField(Field):
    type = datetime.datetime

    def __init__(self, auto_now=False, default=None, blank=False):
        super(DateTimeField, self).__init__(default, blank)
        self.auto_now = auto_now

    def get_default(self):
        return datetime.datetime.now() if self.auto_now else self.default


class ModelMeta(type):

    def __new__(mcs, name, bases, namespace):
        namespace['__fields__'] = {k: v for k, v in namespace.items() if isinstance(v, Field)}

        for k in namespace['__fields__']:
            del namespace[k]

        return super(ModelMeta, mcs).__new__(mcs, name, bases, namespace)


class Model(object):
    __metaclass__ = ModelMeta
    __fields__ = None

    def __init__(self, **kwargs):
        defaults = {k: f.get_default() for k, f in self.__fields__.items()}

        for key, value in kwargs.items():
            assert key in defaults
            defaults[key] = value

        self.__dict__.update(defaults)

    def validate(self):
        for name, field in self.__fields__.items():
            val = getattr(self, name)
            if not field.validate(val):
                raise ValidationError(name, str(val))

