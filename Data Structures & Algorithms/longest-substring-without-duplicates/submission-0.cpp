
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char>set;
        int left = 0;
       
        int largest_sub = 0;
        for (int i = 0;i< s.size();i++){
            while (set.count(s[i])){
                set.erase(s[left]);
                left += 1;
            }
            set.insert(s[i]);
            largest_sub = max(largest_sub,i - left + 1 );



        }
        return largest_sub;
    }
};