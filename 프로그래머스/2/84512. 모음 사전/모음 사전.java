class Solution {
    public int solution(String word) {
        int[] w = {781, 156, 31, 6, 1};
        String vowels = "AEIOU";
        
        int ans = 0;
        for (int i = 0; i < word.length(); i++) {
            int idx = vowels.indexOf(word.charAt(i));
            ans += idx * w[i] + 1;
        }
        return ans;
    }
}