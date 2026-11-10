class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sCount = new int[26];
        int[] tCount = new int[26];

        for(int i = 0; i < s.length(); ++i) {
            sCount[s.charAt(i) - 'a']++;
        }

        for(int i = 0; i < t.length(); ++i) {
            tCount[t.charAt(i) - 'a']++;
        }

        boolean ans = true;

        for(int i = 0; i < sCount.length; ++i) {
            if(sCount[i] != tCount[i]) {
                ans = false; break;
            }
        }

        return ans;

    }
}
