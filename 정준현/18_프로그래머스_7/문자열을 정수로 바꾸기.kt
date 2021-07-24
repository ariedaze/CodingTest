class Solution {
    fun solution(s: String): Int {
        when (s[0]) {
            '+' -> return s.slice(1 until s.length).toInt()
            '-' -> return -1 * s.slice(1 until s.length).toInt()
            else -> return s.toInt()
        }
    }
}