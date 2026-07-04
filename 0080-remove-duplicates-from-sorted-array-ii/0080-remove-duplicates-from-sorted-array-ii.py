class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0  # write pointer: next position to write into

        for num in nums:
            # Write this number if:
            # - We have fewer than 2 elements written yet (k < 2), OR
            # - It differs from the element 2 positions back (nums[k-2]),
            #   meaning we haven't yet placed 2 copies of this value
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1

        return k