class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        S = []

        word = 1
        while(a < A and b < B):
            if word == 1:
                S.append(word1[a])
                a += 1
                word = 2
            else:
                S.append(word2[b])
                b += 1
                word = 1
        
        while(a < A):
            S.append(word1[a])
            a += 1
        
        while(b < B):
            S.append(word2[b])
            b += 1
        
        return ''.join(S)

        # Time: O(A + B)
        # Space: O(A + B)