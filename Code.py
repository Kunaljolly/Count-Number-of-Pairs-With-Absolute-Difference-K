class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        c = 0

        for num in nums:
            if num + k in count:
                c += count[num + k]
        return c
