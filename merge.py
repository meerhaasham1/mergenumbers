class Solution:  #this line defines a Python class named solution
    def merge_alternatively(self, word1, word2): 
        merged = []  #initializes an empty list 
        i, j = 0, 0  #initializes two variables name i and j to 0

        while i < len(word1) or j < len(word2):  #loop will run utill the provided boundary case reaches
            if i < len(word1):
                merged.append(word1[i])
                i += 1
            if j < len(word2):
                merged.append(word2[j])
                j += 1

        return ''.join(merged)         # Convert the merged list of characters into a single string

word1 = 'abc'
word2 = 'bcf'
solution_words = Solution() 
result = solution_words.merge_alternatively(word1, word2)
print(result)
