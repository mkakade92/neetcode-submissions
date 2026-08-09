class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        l =  len(beginWord)
        s = {}
        # Basically create a dictionary of index: set_of_all_letters_on_index
        for word in words:
            for i in range(l):
                if i not in s: 
                    s[i]= set()
                s[i].add(word[i])

        q = deque()
        q.append(beginWord)
        shortest = 0
        visited = set()
        visited.add(beginWord)
        while q:
            shortest+=1

            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return shortest
                for idx,char in enumerate(curr):
                    for letter in s[idx]:
                        if letter != char:
                            nextWord = curr[:idx]+letter+curr[idx+1:]
                            if nextWord in words and nextWord not in visited:
                                q.append(nextWord)
                                visited.add(nextWord)

        return 0