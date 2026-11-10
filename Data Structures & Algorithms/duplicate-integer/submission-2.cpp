class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> check;

        for(auto &x: nums) {
            if(check.find(x) == check.end()) {
                check.insert(x);
            } else {
                return true;
            }
        }

        return false;
    }
};