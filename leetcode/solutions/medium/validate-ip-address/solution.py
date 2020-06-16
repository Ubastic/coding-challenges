from ipaddress import IPv4Address, IPv6Address
from re import search

class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            assert not search(r"0\d", IP)
            ip = IPv4Address(IP)
            return "IPv4"
        except:
            try:
                assert not search(r"::", IP)
                IPv6Address(IP)
                return "IPv6"
            except:
                return "Neither"