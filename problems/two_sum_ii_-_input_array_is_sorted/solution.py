class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            if numbers[i] not in hashmap:
                hashmap[numbers[i]] = i
            complement = target - numbers[i]
            if complement in hashmap and hashmap[complement] != i:
                return [hashmap[complement]+1,i+1]
            