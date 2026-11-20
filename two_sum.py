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
        next_val = 0
        # Start iterating
        for curr in nums:
            for next_val in nums:
                # If the current position plus the next one == target, you win
                if nums[curr] + nums[next_val] == target:
                    return final_answer[curr, next_val]
        return final_answer