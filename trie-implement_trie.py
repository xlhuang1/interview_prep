# Implement a Trie with three functions:
# insert(word: str)
# search(word: str) -> bool
# startsWith(prefix: str) -> bool

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self, root):
        self.root = root

    def insert(self, word):
        curr_node = self.root
        for c in word:
            if c not in curr_node.children.keys():
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.is_end_of_word = True

    def search(self, word):
        curr_node = self.root
        for c in word:
            if c not in curr_node.children.keys():
                return False
            curr_node = curr_node.children[c]
        return curr_node.is_end_of_word

    def startsWith(self, prefix):
        curr_node = self.root
        for c in prefix:
            if c in curr_node.children.keys():
                curr_node = curr_node.children[c]
            else:
                return False
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                # at end of word
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0 #safe to delete if True

            c = word[depth]
            if c not in node.children:
                return False
            should_delete_child = _delete(node.children[c], word, depth+1)
            if should_delete_child:
                del node.children[c]
                return not node.is_end_of_word and len(node.children) == 0

            return False
        _delete(self.root, word, 0)

