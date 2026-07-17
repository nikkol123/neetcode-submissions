from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = Counter(nums)
        nums.sort()
        out = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                needed = 1
                target = -(nums[i] + nums[j])

                if target == nums[i]:
                    needed += 1
                if target == nums[j]:
                    needed += 1

                if d[target] >= needed:
                    triplet = tuple(sorted([nums[i], nums[j], target]))
                    out.add(triplet)

        return [list(t) for t in out]