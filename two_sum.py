class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Given
        # (int) list[]
        # (int) target

        # Return
        # indices of two numbers equaling "target"
        # (int) list[]

        final_answer = list[0,0]
        
        # Brute Force: start from element one of the list, and check it's addition
        # against every other element until either the target is found,
        # or we move onto list[i+1]

        # Brute Force
        # Outer loop: starting point to check addition from
        for curr in range(len(nums)):
            # Inner loop: checking every element's addition
            # against the starting point
            for next_val in range(curr+1, len(nums)):
                # If the current position plus the next one == target, you win
                if nums[curr] + nums[next_val] == target:
                    return [curr, next_val]
        return final_answer