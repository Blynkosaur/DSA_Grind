class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
           map<int,int> hash;
        for(int i= 0; i < nums.size(); i++){
            int complement = target - nums[i];
            if (hash.find(complement) != hash.end()&& hash[complement] != i){
            return {hash[complement], i};
            }else{
            hash[nums[i]] = i;
            }
    

        }
        return {0,1};
    }
};