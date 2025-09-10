#solution 1: my own try
# 39th percentile runtime, 95th percentile memory
# TC: O(N^2), SC: O(n)
def replaceWords(dictionary: list[str], sentence: str) -> str:
	#Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
	#Output: "the cat was rat by the bat"
	# 1. order strings by length
	# 2. split sentence and check each word
	# print out result
	result = []
	dictionary = sorted(dictionary,key=len)
	sentence = sentence.split()
	for word in sentence:
		found = False
		for check_word in dictionary:
			if word.startswith(check_word):
				if check_word in word:
					result.append(check_word)
					found = True
					break
		if not found:
			result.append(word)
	return " ".join(result)


#solution2: using a trie node system
# 65th percentile runtime, 48th percentile memory
# TC: O(NL + M * L'), n is number of roots, l is length of root, m in # words in sentence, L' is avg length of word, SC: O(NL + M * L')
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word):
        node = self.root
        prefix = ''
        for char in word:
            if char not in node.children:
                return word
            prefix += char
            if node.children[char].isEnd:
                return prefix
            node = node.children[char]
        return word

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        result = []
        for word in sentence.split():
            result.append(trie.search(word))
        
        return ' '.join(result)

dictionary = ["a","b","c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(replaceWords(dictionary,sentence))