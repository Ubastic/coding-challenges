import re

def validPhoneNumber(phoneNumber):
    return re.fullmatch(r'\(\d{3}\) \d{3}-\d{4}', phoneNumber) is not None