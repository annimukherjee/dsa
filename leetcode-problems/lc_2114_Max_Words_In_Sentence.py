class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        max_words = -1
        for sentence in sentences:
            words = len(sentence.split())

            if words > max_words:
                max_words = words
        
        return max_words