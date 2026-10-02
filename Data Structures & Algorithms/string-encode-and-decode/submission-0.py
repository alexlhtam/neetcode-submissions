class Solution:

    def encode(self, strs: List[str]) -> str:

        def enc_word(word) -> str:
            n = len(word)
            res = str(n) + "#" + word
            return res

        res = ""
        for word in strs:
            res += enc_word(word)

        return res

    def decode(self, s: str) -> List[str]:
        encoded_words = list(s)

        res = [] 

        i = 0
        while i < len(encoded_words):
            j = i
            while encoded_words[j] != "#":
                j += 1
            n = int("".join(encoded_words[i:j]))
            word = "".join(encoded_words[j+1:j+n+1])
            res.append(word)
            i  = j + n + 1

        return res