class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset
        # loop through the array
        # if we find a dup, return true
        # else add it to the set

        numset = set()

        for n in nums:
            if n in numset:
                return True
            numset.add(n)
        return False