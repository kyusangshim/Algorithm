import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        
        // pq 생성 및 값 담기
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) {
            pq.add(s);
        }
        
        // 가장 낮은거 두개 뽑아서 다시 넣기
        int count = 0;
        while (pq.peek() < K) {
            if (pq.size() < 2) return -1;
            
            int first = pq.poll();
            int second = pq.poll();
            int mixed = first + second*2;
            
            pq.add(mixed);
            count++;
        }
        
        return count;
    }
}