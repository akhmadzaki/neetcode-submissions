class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        Set<Integer> zeroIndex = new HashSet<>();
        int mult = 1;

        for(int i = 0; i < nums.length; ++i) {
            if(nums[i] == 0) {
                zeroIndex.add(i);
                continue;
            } else {
                mult *= nums[i];
            }
        }

        for(int i = 0; i < nums.length; ++i) {
            if(nums[i] == 0 && zeroIndex.size() > 1) {
                ans[i] = 0;
            } else if(nums[i] != 0 && zeroIndex.size() > 0) {
                ans[i] = 0;
            } else if(nums[i] == 0 && zeroIndex.size() == 1) {
                ans[i] = mult;
            } else {
                ans[i] = mult/nums[i];
            }
        }

        return ans;
    }
}  
