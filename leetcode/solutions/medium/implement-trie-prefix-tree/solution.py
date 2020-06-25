class Trie:

    def __init__(self, letter=None):
        """
        Initialize your data structure here.
        """
        self.nodes = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.nodes
        for c in word:
            temp = temp.setdefault(c, {})
        temp['end'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.nodes
        for c in word:
            if c not in temp:
                return False
            temp = temp[c]

        return 'end' in temp
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.nodes
        for c in prefix:
            if c not in temp:
                return False
            temp = temp[c]

        return True