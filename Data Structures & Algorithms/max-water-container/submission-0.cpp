class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int area = 0;
        int max = 0;
        while (left < right){
            area = min(heights[left],heights[right]) * (right - left);
            if (area > max){
                max = area;
            }
            if(heights[left] < heights[right]){
                left ++;
            }
            else{
                right --;
            }
        }
        return max;
    }
};
