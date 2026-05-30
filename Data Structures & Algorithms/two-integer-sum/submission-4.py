class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # comp
        # hashmap
        numsmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numsmap:
                return [numsmap[comp], i]
            numsmap[nums[i]] = i
        return []