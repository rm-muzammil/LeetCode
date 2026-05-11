class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        max_water = 0
        while l < r:
            w = r - l
            area = w * min(height[l],height[r])
            max_water = max(max_water,area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_water
