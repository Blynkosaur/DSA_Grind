class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        output = []
        for num in nums: 
            counter[num] = counter.get(num,0) + 1
    
        buckets = [[] for _ in range(len(nums))]
        for num in counter:
            buckets[counter[num]-1].append(num)
        print(f"buckets:{buckets} counter: {counter}")
        for i in range(len(nums)-1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
        return output
        
