class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int equalVal = 0;

        for(auto it = nums.begin(); it != nums.end();) {
            if(*it == val) {
                it = nums.erase(it);
                equalVal++;
            } else {
                ++it;
            }
        }
        return nums.size();
    }
};