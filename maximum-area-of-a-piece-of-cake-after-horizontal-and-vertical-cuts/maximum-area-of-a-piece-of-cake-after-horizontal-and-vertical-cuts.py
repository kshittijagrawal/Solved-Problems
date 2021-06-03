class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hcuts, vcuts = sorted(horizontalCuts), sorted(verticalCuts)
        hmax, vmax = 0, 0
        for i in range(1, len(hcuts)):
            hmax = max(hmax, hcuts[i]-hcuts[i-1])
        for j in range(1, len(vcuts)):
            vmax = max(vmax, vcuts[j]-vcuts[j-1])
        hmax, vmax = max(hmax, hcuts[0], h-hcuts[-1]), max(vmax, vcuts[0], w-vcuts[-1])
        return (hmax*vmax)%1000000007