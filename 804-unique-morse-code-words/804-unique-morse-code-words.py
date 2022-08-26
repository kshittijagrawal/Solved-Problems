class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        container, s = {chr(97 + i) : code[i] for i in range(26)}, set()
        
        for word in words:
            trans = []
            for c in word:
                trans.append(container[c])
            s.add("".join(trans))
            
        return len(s)