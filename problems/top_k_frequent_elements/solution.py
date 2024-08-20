import time
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        time.sleep(0.5)
        hashmap = {}
        reverse_hash = {}
        ret = []
        keys = []
        sort = sorted(nums)
        for el in sort:
            if el not in hashmap:
                hashmap[el] = 1
            else:
                hashmap[el] += 1
        for el in hashmap:
            keys.append(hashmap[el])
        print(hashmap)
        print(f'keys{keys}')
        print(f'sorted keys{sorted(keys)}')
        keys = sorted(keys)
        for i in range(k):
            max_time = keys[-1]
            print(max_time)
            for el in hashmap:
                if hashmap[el] == max_time:
                   
                    ret.append(el)
                    hashmap[el] = 0
                    keys.pop(-1)
                    break

        return ret