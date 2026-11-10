class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int currentNum = nums[0];
        int countDups = 0;
        for(auto it = nums.begin() + 1; it != nums.end();) {
            if(currentNum == *it) {
                countDups++;
                it = nums.erase(it);
            } else {
                currentNum = *it;
                it++;
                
            }
        }

        return nums.size();
    }
};