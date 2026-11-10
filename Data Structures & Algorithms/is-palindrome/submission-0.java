class Solution {
    public boolean isPalindrome(String s) {
        String cleaned = s.chars()
                .filter(Character::isLetterOrDigit) // Keep only letters and digits
                .mapToObj(c -> String.valueOf((char) c)) // Convert int to char
                .collect(Collectors.joining()).toLowerCase();

        StringBuilder reversed = new StringBuilder();
        char[] c = s.toCharArray();
        for(int i = (c.length - 1); i >= 0; --i) {
            if(Character.isLetterOrDigit(c[i])) {
                reversed.append(c[i]);
            }
        }
        return cleaned.equals(reversed.toString().toLowerCase());
        
    }
}
