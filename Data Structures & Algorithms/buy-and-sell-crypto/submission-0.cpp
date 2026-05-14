class Solution {
public:
    int maxProfit(vector<int>& prices) {
        unordered_set<int> set;
        int left = 0;
        int largest_p = 0;
        for (int right = 0; right < prices.size();right ++){
            while (prices[right] < prices[left]){
                set.erase(prices[left]);
                left ++;
                
            }
            prices[right]++;
            largest_p = max(largest_p,prices[right] - prices[left] );
        }
        return largest_p;
    }
};
