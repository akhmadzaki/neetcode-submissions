class Solution {
public:
    bool isPalindrome(string s) {
        for(auto it = s.begin(); it != s.end();) {
            if(!isalnum(*it)) {
                it = s.erase(it);
            } else {
                *it = tolower(*it);
                it++;
            }
        }
        // cout << s << endl;
        int middle = s.size()/2;
        int len = s.size();
        if(s.size() == 0) return true;
        if(s.size() == 1) return true;
        // if(s.size() == 2 && s[0] == s[1]) return true;
        // if(s.size() == 2 && s[0] != s[1]) return false;

        for(int i = 0; i < middle; ++i) {
            if(s[i] != s[len-i-1]) {
                return false;
            }
        }

        return true;
    }
};
