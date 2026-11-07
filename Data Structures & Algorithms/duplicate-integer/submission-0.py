class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i in range(len(nums)):
            num = hash_map.get(nums[i])
            if num is not None:
                return True

            hash_map[nums[i]] = i 
        
        return False
        