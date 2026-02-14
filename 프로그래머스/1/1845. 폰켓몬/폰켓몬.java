import java.util.*;

class Solution {
    public int solution(int[] nums) {
        boolean DEBUG = true;
        
        int k = nums.length / 2;
        HashSet<Integer> set = new HashSet<>();
        
        for (int x: nums) set.add(x);
        
        if (DEBUG) System.out.println("setSize=" + set.size());
        
        return Math.min(set.size(), k);
    }
}