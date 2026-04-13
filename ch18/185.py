# Longest Word
# Write a function taking input
# Input path to text file
# Returns longest Word 
class LongestWord:
    def longestword(self):
        with open("data/neuromancer.txt",'r',encoding='utf-8') as longestword:
            words = longestword.read().split()
            print(len(words))
            print(len(max(words, key=len, default=" ")))
            print(max(words,key=len,default=" "))

words = LongestWord().longestword()
print(words)