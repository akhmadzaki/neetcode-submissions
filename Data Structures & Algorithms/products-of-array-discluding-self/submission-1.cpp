class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size(), 0);

        int total = 1;
        int zeroCount = 0;
        for(auto &x: nums) {
            if(x != 0) total *= x;
            else zeroCount++;
        }

        for(int i = 0; i < ans.size(); ++i) {
            if(nums[i] != 0 && zeroCount) {
                ans[i] = 0;
            } else if(nums[i] == 0 && zeroCount > 1) {
                ans[i] = 0;
            } else if(nums[i] == 0 && zeroCount == 1) {
                ans[i] = total;
            } else {
                ans[i] = total / nums[i];
            }
        }

        return ans;
    }
};
