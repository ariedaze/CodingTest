class Solution {
    fun solution(n: Int): String {
        val stringBuilder = StringBuilder()
        stringBuilder.append("수박".repeat(n / 2))
        if (n % 2 == 1) { stringBuilder.append("수") }
        return stringBuilder.toString()
    }
}