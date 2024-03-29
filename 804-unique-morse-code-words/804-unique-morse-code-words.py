class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        container, s = {chr(97 + i) : code[i] for i in range(26)}, set()
        
        for word in words:
            trans = ""
            for c in word:
                trans += container[c]
            s.add(trans)
            
        return len(s)