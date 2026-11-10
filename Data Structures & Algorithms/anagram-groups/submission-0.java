class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hm = new HashMap<>();

        for(String s: strs) {
            int[] a = new int[26];
            for(char c: s.toCharArray()) {
                a[c-'a']++;
            }

            StringBuilder key = new StringBuilder();
            for(int i = 0; i < a.length; ++i) {
                for(int j = 0; j < a[i]; ++j){
                    key.append('a' + i);
                }
            }
            

            if(!hm.containsKey(key.toString())) hm.put(key.toString(), new ArrayList<String>());
            hm.get(key.toString()).add(s);
        }

        List<List<String>> ans = new ArrayList<>();
        for (List<String> entry : hm.values()) {
            ans.add(entry);
        }

        return ans;
    }
}
