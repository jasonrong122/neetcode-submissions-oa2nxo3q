class PrefixTree:

    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.trie:
            if prefix in word[:len(prefix)]:
                return True

        return False
