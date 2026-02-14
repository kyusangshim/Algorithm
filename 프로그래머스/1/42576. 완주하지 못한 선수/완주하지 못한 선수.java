import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {        
        // HashMap 생성
        HashMap<String, Integer> map = new HashMap<>();
        
        // 참가자 count
        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }
        
        // 완주자 count
        for (String c : completion) {
            map.put(c, map.get(c)-1);
        }
        
        for (Map.Entry<String, Integer> e : map.entrySet()) {
            if (e.getValue() != 0) return e.getKey();
        }
        
        return "";
    }
}