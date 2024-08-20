class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for i in strs:
            ls = []
            for j in range(len(i)):
                
                ls.append(i[j])
            
            s_s = sorted((ls))
            s = "".join(s_s)
            if s in hashmap:
                hashmap[s].append(i)
            else:
                hashmap[s] = [i]
        return hashmap.values()
        
            
               