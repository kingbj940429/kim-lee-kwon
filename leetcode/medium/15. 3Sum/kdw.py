class Solution:
    # Hash Table
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        n = len(nums)
        dic = {num: i for i, num in enumerate(nums)}
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                target = -(nums[i] + nums[j])
                if target in dic and j < dic[target]:
                    triplets.add((nums[i], nums[j], target))
        return list(triplets)

    # Two Pointers
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return list(triplets)
