class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        outputs = set()
        for i in range(len(nums)):
            copy = nums.copy()
            copy.remove(nums[i])
            for num in copy:
                second_copy = copy.copy()
                second_copy.remove(num)
                left = 0
                right = len(second_copy)-1
                complement = target - num - nums[i]
                while left < right:
                    if second_copy[left] + second_copy[right] == complement:
                        outputs.add(tuple(sorted([second_copy[left], second_copy[right],num, nums[i]])))
                        right -= 1
                        left += 1
                    elif second_copy[left] + second_copy[right] > complement:
                        right -= 1
                    else:
                        left += 1
        
        
        
        return [list(tuple_el) for tuple_el in outputs]
                    

                
