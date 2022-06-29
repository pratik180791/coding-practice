class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        mapped_order = {}
        for i in range(len(order)):
            mapped_order[order[i]] = i

        def compare(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if mapped_order[word1[i]] > mapped_order[word2[i]]:
                    print(word1[i], word2[i])
                    print(mapped_order[word1[i]], mapped_order[word2[i]])
                    return False


        for i in range(len(words)-1):
            if not compare(words[i], words[i + 1]):
                return False
            break
        return True

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
result  = Solution().isAlienSorted(words=words, order=order)
print(result)


def isAlienSorted(self, words, order: str) -> bool:
    mapped_order = {}
    for i in range(len(order)):
        mapped_order[order[i]] = i

    temp = [[mapped_order[c] for c in w] for w in words]
    print(temp)

    for k in range(len(words) - 1):
        word1 = words[k]
        word2 = words[k + 1]
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                if mapped_order[word1[i]] > mapped_order[word2[i]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False
    return True
