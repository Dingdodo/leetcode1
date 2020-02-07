import string
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList=set(wordList)
        if endWord not in wordList:
            return []
        wordList.add(beginWord)
        distance=self.bsf(endWord,wordList)
        res=[]
        self.dfs(beginWord, endWord, wordList, distance, [beginWord], res)

        return res
    # 广度优先搜索 分层 返回分层信息
    def bsf(self,begin_word,wordList):
        #定义队列
        que=[begin_word]
        distance={}
        distance[begin_word]=0
        while que:
            size=len(que)
            for _ in range(size):
                curr_word=que.pop(0)
                next_words=self.get_next_words(curr_word,wordList)
                for next_word in next_words:
                    if next_word not in distance:
                        distance[next_word]=distance[curr_word]+1
                        que.append(next_word)
        print(distance)
        return distance

    # 找到差一个单词的下一个字符串
    def get_next_words(self,curr_word,wordList):
        next_words=[]
        for i in range(len(curr_word)):
            for c in list(string.ascii_lowercase):
                next_word=curr_word[:i]+c+curr_word[i+1:]
                if next_word in wordList and next_word!=curr_word:
                    next_words.append(next_word)
        return next_words

    # 深度优先搜索
    def dfs(self, curr_word, target, wordList, distance, path, results):

        if curr_word==target:
            results.append(list(path))
            return
        for next_word in self.get_next_words(curr_word,wordList):

            if distance[next_word]!=distance[curr_word]-1:
                continue

            path.append(next_word)
            self.dfs(next_word, target, wordList, distance, path, results)
            path.pop()




if __name__=="__main__":
    beginWord = "talk"
    endWord =  "tail"
    wordList =  ["talk", "tons", "fall", "tail", "gale", "hall", "negs"]




    s=Solution()
    print(s.findLadders(beginWord,endWord,wordList))

