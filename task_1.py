
class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for put: key = {key} must be a non-empty string")

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value
        current.is_end_of_word = True

    def get(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for get: key = {key} must be a non-empty string")

        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    def delete(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for delete: key = {key} must be a non-empty string")

        def _delete(node, key, depth):
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    node.is_end_of_word = False
                    self.size -= 1
                    return len(node.children) == 0
                return False

            char = key[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], key, depth + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0 and node.value is None
            return False

        return _delete(self.root, key, 0)

    def is_empty(self):
        return self.size == 0

    def contains(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for contains: key = {key} must be a non-empty string")
        return self.get(key) is not None

    def longest_prefix_of(self, s):
        if not isinstance(s, str) or not s:
            raise TypeError(f"Illegal argument for longestPrefixOf: s = {s} must be a non-empty string")

        current = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in s:
            if char in current.children:
                current = current.children[char]
                current_prefix += char
                if current.value is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix

    def keys_with_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for keysWithPrefix: prefix = {prefix} must be a string")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result = []
        self._collect(current, list(prefix), result)
        return result

    def _collect(self, node, path, result):
        if node.is_end_of_word:
            result.append("".join(path))
        for char, next_node in node.children.items():
            path.append(char)
            self._collect(next_node, path, result)
            path.pop()

    def keys(self):
        result = []
        self._collect(self.root, [], result)
        return result

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError(f"Illegal argument for count_words_with_suffix: pattern = {pattern} must be a string")

        if not pattern:
            return 0

        reversed_pattern = pattern[::-1]

        reversed_trie = self._create_reversed_trie()

        current = reversed_trie.root
        for char in reversed_pattern:
            if char not in current.children:
                return 0
            current = current.children[char]
        return self._count_words(current)

    def _create_reversed_trie(self):
        reversed_trie = Trie()
        all_words = self.keys()

        for word in all_words:
            reversed_word = word[::-1]
            reversed_trie.put(reversed_word, None)

        return reversed_trie

    def _count_words(self, node):
        count = 1 if node.is_end_of_word else 0

        for child in node.children.values():
            count += self._count_words(child)

        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for has_prefix: prefix = {prefix} must be a string")

        if not prefix:
            return False

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True

def task_1():
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)
    print("\nTesting count_words_with_suffix method:")

    result = trie.count_words_with_suffix("e")
    print(f"count_words_with_suffix('e') = {result}")
    assert result == 1

    result = trie.count_words_with_suffix("ion")
    print(f"count_words_with_suffix('ion') = {result}")
    assert result == 1

    result = trie.count_words_with_suffix("a")
    print(f"count_words_with_suffix('a') = {result}")
    assert result == 1

    result = trie.count_words_with_suffix("at")
    print(f"count_words_with_suffix('at') = {result}")
    assert result == 1

    print("\nTesting has_prefix method:")

    result = trie.has_prefix("app")
    print(f"has_prefix('app') = {result}")
    assert result == True

    result = trie.has_prefix("bat")
    print(f"has_prefix('bat') = {result}")
    assert result == False

    result = trie.has_prefix("ban")
    print(f"has_prefix('ban') = {result}")
    assert result == True

    result = trie.has_prefix("ca")
    print(f"has_prefix('ca') = {result}")
    assert result == True

    print("\nAll tests passed!")

if __name__ == '__main__':
    task_1()
