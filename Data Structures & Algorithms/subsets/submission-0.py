class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def helper(i, cur_set, subsets):
            if i >= len(nums):
                subsets.append(cur_set.copy())
                return
            
            cur_set.append(nums[i])
            helper(i+1, cur_set, subsets)

            cur_set.pop()
            helper(i+1, cur_set, subsets)

        helper(0, [], subsets)
        return subsets
