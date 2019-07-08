# coding=utf-8
from itertools import cycle

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = alphabet.decode('utf-8')
        self.key = key.decode('utf-8')
        self.table = [alphabet[i:] + alphabet[:i] for i, _ in enumerate(alphabet)]

    def _encode(self, a, b):
        return self.alphabet[(self.alphabet.index(a) + self.alphabet.index(b)) % len(self.alphabet)]

    def _decode(self, a, b):
        return self.alphabet[(self.alphabet.index(a) - self.alphabet.index(b)) % len(self.alphabet)]

    def encode(self, text):
        return ''.join(
            self._encode(a, b) if a in self.alphabet else a for a, b in zip(text.decode('utf-8'), cycle(self.key))
        ).encode('utf-8')

    def decode(self, text):
        return ''.join(
            self._decode(a, b) if a in self.alphabet else a for a, b in zip(text.decode('utf-8'), cycle(self.key))
        ).encode('utf-8')