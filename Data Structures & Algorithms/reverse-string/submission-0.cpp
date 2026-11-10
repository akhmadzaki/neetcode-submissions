class Solution {
public:
    void reverseString(vector<char>& s) {
        int middle = s.size()/2;
        int len = s.size();

        for(int i = 0; i < middle; ++i) {
            swap(s[i], s[len - i - 1]);
        }        
    }
};