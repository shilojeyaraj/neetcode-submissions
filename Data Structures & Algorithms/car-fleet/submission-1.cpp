class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int,int>> cars;
        
        for (int i = 0;i <n ;i++){
            cars.push_back({position[i],speed[i]});
        }
        sort(cars.begin(),cars.end(), greater<pair<int,int>>());
        stack<double> st;

         for (auto& [pos, spd] : cars) {   //pos = first key, spd = value
            double time = (double)(target - pos) / spd;
            if (st.empty() || time > st.top()) {
                st.push(time);
            }
         }
            return st.size();

    }
};
