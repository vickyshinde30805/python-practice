class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1
        self.best_length = float('inf')


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        
        root = TrieNode()

        # Function to update best answer at node
        def update(node, word_len, index):
            if (word_len < node.best_length or
               (word_len == node.best_length and index < node.best_index)):
                
                node.best_length = word_len
                node.best_index = index

        # Build Trie using reversed words
        for index, word in enumerate(wordsContainer):

            node = root

            # Reverse word for suffix matching
            reversed_word = word[::-1]

            # Update root node
            update(node, len(word), index)

            for ch in reversed_word:

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                update(node, len(word), index)

        answer = []

        # Process queries
        for word in wordsQuery:

            node = root

            reversed_word = word[::-1]

            for ch in reversed_word:

                if ch not in node.children:
                    break

                node = node.children[ch]

            answer.append(node.best_index)

        return answer


# ---------------- DRIVER CODE ----------------

wordsContainer = ["abcd", "bcd", "xbcd"]
wordsQuery = ["cd", "bcd", "xyz"]

obj = Solution()

print(obj.stringIndices(wordsContainer, wordsQuery))