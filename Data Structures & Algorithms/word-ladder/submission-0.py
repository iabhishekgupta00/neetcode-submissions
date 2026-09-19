from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in words:
                        words.remove(newWord)
                        q.append((newWord, steps + 1))

        return 0