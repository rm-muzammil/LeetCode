class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0] +  nums[1] + nums[2]

        for i in range(len(nums) -2):

            l,r = i +1, len(nums) -1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                # exact answer
                if curr_sum == target:
                    return curr_sum

                elif curr_sum < target:
                    l += 1

                else:
                    r -= 1
        return closest