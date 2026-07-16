class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        char[] aSort = s.toCharArray();
        char[] tSort = t.toCharArray();
        Arrays.sort(aSort);
        Arrays.sort(tSort);

        return Arrays.equals(aSort, tSort);
    }
}
