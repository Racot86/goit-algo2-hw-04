from task_1 import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        if not all(isinstance(s, str) for s in strings):
            return ""

        if len(strings) == 1:
            return strings[0]

        min_length = min(len(s) for s in strings)

        common_prefix = []
        for i in range(min_length):
            current_char = strings[0][i]
            if all(s[i] == current_char for s in strings):
                common_prefix.append(current_char)
            else:
                break

        return ''.join(common_prefix)

if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["hello", 123, True]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["singleword"]
    assert trie.find_longest_common_word(strings) == "singleword"

    trie = LongestCommonWord()
    strings = ["prefix", "prefixextra", "prefixmore"]
    assert trie.find_longest_common_word(strings) == "prefix"

    print("All tests passed!")
