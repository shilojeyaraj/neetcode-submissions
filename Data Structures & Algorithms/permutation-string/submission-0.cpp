class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> count1;
        int left = 0;
        int size1 = s1.size();
        unordered_map<char,int> count2;

        for(int mini = 0; mini < size1;mini++){
            count1[s1[mini]]++;
            count2[s2[mini]]++;
        }
        if (count1 == count2){
            return true;
        }

        for (int right = size1;right < s2.size(); right ++){
           
            count2[s2[right]] ++;
            int left = right - size1;
            count2[s2[left]]--;

            
            if(count2[s2[left]] == 0){
                count2.erase(s2[left]);
            }

            if (count1 == count2){
                return true;
            

            }
        }
         return false;   
    }
};
