class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int i = 0;
        string longestPrefix = "";

        sort(strs.begin(), strs.end(), [](string a, string b) 
        {
            return a.size() < b.size();
        });

        if(strs[0].size() == 0) return "";
        
        int shortestLen = strs[0].size();
        string shortestStr = strs[0];
        bool breakOuter = false;
        
        for(int i = 0; i < shortestLen; ++i) {
            char c = shortestStr[i];

            for(auto &x: strs) {
                if(x[i] != c) {
                    breakOuter = true;
                }
            }
            if(breakOuter) break;

            longestPrefix.push_back(c);
        }

        return longestPrefix;
    }
};