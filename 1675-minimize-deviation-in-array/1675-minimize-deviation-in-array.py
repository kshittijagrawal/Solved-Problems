import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap = []
        maxHeap = []
        for n in nums:
            heapq.heappush(minHeap,n)
            heapq.heappush(maxHeap,-n)
        ans = abs(-maxHeap[0] - minHeap[0])
        
        while minHeap[0] % 2 == 1:
            minVal = 2 * heapq.heappop(minHeap)
            heapq.heappush(minHeap,minVal)
            heapq.heappush(maxHeap,-minVal)
            ans = min(ans, abs(-maxHeap[0] - minHeap[0]))
            
        while (-maxHeap[0]) % 2 == 0:
            maxVal = heapq.heappop(maxHeap)//2
            heapq.heappush(maxHeap,maxVal)
            heapq.heappush(minHeap,-maxVal)
            ans = min(ans, abs(-maxHeap[0] - minHeap[0]))
        
        return ans