class Solution {
    public int hammingWeight(int n) {
        int bitsCount = 0;
        while(n > 0) {
            if((n & 1) == 1) bitsCount++;
            n = n >> 1;
        }
        System.out.println(bitsCount);
        return bitsCount;
    }
}
