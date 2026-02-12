class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> need = new HashMap<>(); // counter map of t {'A':1, 'B':1 ...}
        for (int i = 0; i < t.length(); i++) { // fill need map
            char c = t.charAt(i);
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int required = need.size(); // number of chars to satisfy
        int formed = 0; //how many are currently satisfied

        HashMap<Character, Integer> window = new HashMap<>();

        int l = 0;
        int bestLen = Integer.MAX_VALUE;
        int bestL = 0;

        for(int r = 0; r<s.length();r++){
            char c = s.charAt(r);
            window.put(c, window.getOrDefault(c, 0) + 1);
            if (need.containsKey(c) && window.get(c).intValue() == need.get(c).intValue()) {
                formed++;
            }
            while (l <= r && formed == required) {
                int len = r - l + 1;
                if (len < bestLen) {
                    bestLen = len;
                    bestL = l;
                }
                // try to shrink window from left
                char leftChar = s.charAt(l);
                window.put(leftChar, window.get(leftChar) - 1);
                
                // is valid ?
                if (need.containsKey(leftChar) && window.get(leftChar) < need.get(leftChar)) {
                    formed--; // no longer valid - won't enter loop on next iter
                }

                l++;

            }
        }
        return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestL, bestL + bestLen);
    }
}