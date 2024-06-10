def anagram(word1,word2):
     word1.sort()
     word2.sort()
     if word1==word2:
          return "anagram"
     else:
          return "not anagram"
          
word1=list("listen")
word2=list("silent")
print(anagram(word1,word2))