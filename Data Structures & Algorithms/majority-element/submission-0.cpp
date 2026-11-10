class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int currentVal = 0,currentCount = 1,maxVal = 0,maxCount = 1;
        if(nums.size() == 1) return nums[0];

        for(int i = 1; i < nums.size(); ++i) {
            if(nums[i] == nums[i-1]) {
                currentVal = nums[i];
                currentCount++;
            } else {
                if(currentCount > maxCount) {
                    maxVal = nums[i-1];
                    maxCount = currentCount;
                }
                currentVal = nums[i];
                currentCount = 1;
            }
        }
        if(currentCount > maxCount) {
            maxCount = currentCount;
            maxVal = nums[nums.size()-1];
        }
        return maxVal;
    }
};