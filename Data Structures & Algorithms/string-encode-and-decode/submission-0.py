class Solution:

    def encode(self, strs: List[str]) -> str:
        self.hashmap = {}
        encoded_string = ""
        for i in range(len(strs)):
            self.hashmap[i] = strs[i]
            encoded_string += strs[i]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        arr = []
        for k, v in self.hashmap.items():
            arr.append(v)

        return arr