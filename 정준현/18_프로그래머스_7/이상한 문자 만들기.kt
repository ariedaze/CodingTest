class Solution {
    fun solution(s: String): String {
        var isEven = true
        var stringBuilder = StringBuilder()
        for (ch in s) {
            if (ch == ' ') {
                stringBuilder.append(ch)
                isEven = true
            } else {
                if (isEven) {
                    stringBuilder.append(ch.toUpperCase())
                } else {
                    stringBuilder.append(ch.toLowerCase())
                }
                isEven = !isEven
            }
        }

        return stringBuilder.toString()
    }
}