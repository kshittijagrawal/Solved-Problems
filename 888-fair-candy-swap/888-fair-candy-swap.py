class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alicesum, container, bobsum = 0, set(), sum(bobSizes)
        for a in aliceSizes:
            alicesum += a
            container.add(a)
        
        for b in bobSizes:
            if ((alicesum - bobsum)//2 + b) in container:
                return [(alicesum - bobsum)//2 + b, b]