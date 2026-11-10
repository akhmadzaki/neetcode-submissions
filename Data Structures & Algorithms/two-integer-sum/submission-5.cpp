class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        multimap<int,int> m;
        vector<int> ans;
        
        for(int i = 0; i < nums.size(); ++i) {
            m.insert(make_pair(nums[i], i));
        }

        bool breakOuterLoop = false;

        for(int i = 1; i < nums.size(); ++i) {
            int key = target - nums[i];
            if(m.find(key) != m.end()) {
                for(auto it = m.lower_bound(key); it != m.upper_bound(key); ++it) {
                    if(it->second != i) {
                        ans.push_back(i);
                        ans.push_back(it->second);
                        breakOuterLoop = true;
                        break;
                    }
                }
                if(breakOuterLoop) break;
            }
        }

        sort(ans.begin(), ans.end());

        return ans;
        
    }
};
