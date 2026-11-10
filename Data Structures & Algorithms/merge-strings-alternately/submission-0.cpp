class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ans = "";
        int min_len = min(word1.size(), word2.size());
        int rest_len = max(word1.size()-min_len, word2.size()-min_len);

        for(int i = 0; i < min_len; ++i) {
            ans.push_back(word1[i]);
            ans.push_back(word2[i]);
        }

        if(word1.size() > word2.size()) {
            ans.append(word1.substr(min_len, rest_len));
        } else if(word2.size() > word1.size()) {
            ans.append(word2.substr(min_len, rest_len));
        } 

        return ans;
    }
};