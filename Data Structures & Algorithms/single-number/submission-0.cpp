class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_set<int> set;
        for(int i = 0;i< nums.size();i++){
            if(set.count(nums[i])){
                set.erase(nums[i]);
            }
            else{
            set.insert(nums[i]);
            }
        }
        return *set.begin();
    }
};
