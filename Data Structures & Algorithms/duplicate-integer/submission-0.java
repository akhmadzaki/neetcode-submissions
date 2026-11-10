class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int i = 0; i < nums.length; ++i) {
            if(hm.get(nums[i]) == null) hm.put(nums[i], 1);
            else hm.put(nums[i], hm.get(nums[i])+1);
        }

        boolean ans = false;

        for(int i = 0; i < nums.length; ++i) {
            if(hm.get(nums[i]) > 1) {
                ans = true; break;
            }
        }

        return ans;
    }
}
