import java.util.*;

class Solution {
    public static int findMax(int[] arr) {
        int currentMax = -1;
        for (int i = 0; i < arr.length; i++) {
            if (currentMax < arr[i]) currentMax = arr[i];
        }
        return currentMax;
    }
    
    public static int findIdx(int len, int idx) {
        idx++;
        return idx % len;
    }
    
    public int solution(int[] priorities, int location) {
        
        int n = priorities.length;
        int maxVal = findMax(priorities);
        int idx = 0;
        int count = 0;
        
        while (true) {            
            if (maxVal == priorities[idx]) {
                count++;
                if (idx == location) {
                    return count;
                }
                else {
                    priorities[idx] = 0;
                    maxVal = findMax(priorities);
                }
            } 
            idx = findIdx(n, idx);
        }
        
    }
}