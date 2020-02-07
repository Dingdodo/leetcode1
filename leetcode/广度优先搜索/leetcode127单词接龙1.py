import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        l = len(endWord)
        ws = set(wordList)

        head = {beginWord}
        tail = {endWord}
        res = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head

            q = set()
            for cur in head:
                for i in range(l):
                    for c in list(string.ascii_lowercase):
                        word = cur[:i] + c + cur[i + 1:]
                        if word in tail:
                            return res + 1
                        if word in ws:
                            q.add(word)
                            ws.remove(word)
            head = q
            res += 1

        return 0

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet=set(wordList)
        curr_word=[beginWord]
        higth=1

        next_words=[]

        while curr_word:
            for word in curr_word:
                if word==endWord:
                    return higth
                for i in range(len(word)):
                    for c in list(string.ascii_lowercase):
                        new_word=word[:i]+c+word[:i+1]
                        if new_word in wordSet:
                            wordSet.remove(new_word)
                            next_words.append(new_word)
            curr_word=next_words
            next_words=[]
            higth+=1
        return 0

    # 两端广度
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        begin_word = {beginWord}
        end_word ={endWord}
        higth = 1

        while begin_word:
            print("===========================")
            print(begin_word)

            print(end_word)
            print("===========================")
            if len(begin_word)>len(end_word):
                begin_word ,end_word=end_word,begin_word
                print("0000000000000000000000000")
                print(begin_word)

                print(end_word)
                print("00000000000000000000000000000")
            temp=set()
            for word in begin_word:
                # if word == endWord:
                #     return higth
                for i in range(len(word)):
                    for c in list(string.ascii_lowercase):
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in end_word:
                            return higth+1
                        if new_word in wordSet:
                            temp.add(new_word)
                            wordSet.remove(new_word)


            begin_word = temp
            higth += 1
        return 0


    # 找到差一个单词的下一个字符串
    def get_next_words(self, curr_word, wordList):
        new_words=[]
        for i in range(len(curr_word)):
            for c in list(string.ascii_lowercase):
                new_word=curr_word[:i]+c+curr_word[i+1:]
                if new_word in wordList and  new_words!=curr_word:
                    new_words.append(new_word)
        return new_words

        # 深度优先搜索



if __name__=="__main__":

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    s=Solution()
    ans=s.ladderLength2(beginWord,endWord,wordList)
    print(ans)
