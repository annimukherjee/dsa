class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_str = "abcdefghijklmnopqrstuvwxyz"
        for i in alphabet_str:
            if i not in sentence:
                return False
        
        return True