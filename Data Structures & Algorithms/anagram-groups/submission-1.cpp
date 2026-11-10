class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> m;
        vector<vector<string>> ans;
        string key;

        for(auto& x: strs) {
            key = x;
            sort(key.begin(), key.end());
            m[key].push_back(x);
        }

        vector<string> v;
        
        for(auto &x: m) {
            v.clear();
            for(auto &y: x.second) {
                v.push_back(y);
            }
            ans.push_back(v);
        }
        return ans;
    }
};
