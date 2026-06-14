class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix products
        # left_prefix = []
        # right_prefix = []
        final_products = [1 for i in range(len(nums))]
        """[1,2,3,4,5]
            [1,1,2,6,24]
            []
        
        n =5
            [120,60,40,30,24]
        left [1,2,6,24,120]
        right [5,20,60,120,120]
        
        """
        curr_prod = 1
        for i in range(len(nums)-1):
            curr_prod*=nums[i]
            final_products[i+1] *= curr_prod

        curr_prod = 1
        for i in range(len(nums)-1,0,-1):
            curr_prod*=nums[i]
            final_products[i-1] *= curr_prod
             
        # left_prod = 1
        # right_prod = 1
        # for i in range(len(nums)):
        #     left_prod *= nums[i] 
        #     left_prefix.append(left_prod)
        #     right_prod *= nums[len(nums)-1-i]
        #     right_prefix.append(right_prod)
        # print(left_prefix, right_prefix)

        # for i in range(len(nums)):
        #     curr_prod = 1
        #     left_index = i-1
        #     right_index = len(nums)-i-2
        #     print(f"left: {left_index} right:{right_index}")
        #     curr_prod = curr_prod*left_prefix[left_index] if left_index >= 0 else curr_prod 
        #     curr_prod = curr_prod*right_prefix[right_index] if right_index >= 0 else curr_prod 
        #     final_products.append(curr_prod)
        return final_products

            


        
        
        



        