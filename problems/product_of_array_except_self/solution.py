import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        left = [1]
        right = [1]
        left_prod = 1
        right_prod = 1
        left_count = 1
        right_count = -1
        for i in range(len(nums)-1):
            left_prod *= nums[left_count-1]
            left.append(left_prod)
            left_count += 1
            right_prod *= nums[right_count]
            right.append(right_prod)
            right_count -= 1

        print(left)
        print(right)

        
        right.reverse()
        # prod = 1
        # for i in range(1,len(nums)):
        #     prod *= nums[i-1]
        #     right.append(prod)
        # right.reverse()
        
        for i in range(len(nums)):
            out.append(left[i]*right[i])
       

        

           
        return out

        