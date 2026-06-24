class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        outputs = set() 
        nums.sort()

        for i in range(len(nums)):
            target = -1 * nums[i]
            left = 0
            right = len(nums)-1

            if nums[left] + nums[left+1] > target:
                continue

            elif nums[right] + nums[right-1] < target:
                continue

            else:
                while left < right:
                    if left == i:
                        left += 1
                        continue
                    elif right == i:
                        right -= 1
                        continue

                    elif nums[left] + nums[right] == target:
                        outputs.add(tuple(sorted([nums[i],nums[left],nums[right]])))
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        right -= 1
                        while left<right and nums[right] == nums[right+1]:
                            right -= 1

                    elif nums[left] + nums[right] < target:
                        left += 1

                    else:
                        right -= 1

        return [list(out) for out in outputs]

