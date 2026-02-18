class Solution {    
    public int solution(int[][] sizes) {
        int maxBig = 0;
        int maxSmall = 0;
        
        for (int[] s : sizes) {
            int w = s[0], h = s[1];
            int big = Math.max(w, h);
            int small = Math.min(w, h);
            
            if (big > maxBig) maxBig = big;
            if (small > maxSmall) maxSmall = small;
        }
        
        return maxBig * maxSmall;
    }
}