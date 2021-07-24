class Solution {
    fun solution(s: String, n: Int): String {
        val stringBuilder = StringBuilder()

        s.forEach {
            when (it.toInt()) {
                in 65..90 -> stringBuilder.append(((it.toInt() - 65 + n) % 26 + 65).toChar())
                in 97..122 -> stringBuilder.append(((it.toInt() - 97 + n) % 26 + 97).toChar())
                else -> stringBuilder.append(' ')
            }
        }

        return stringBuilder.toString()
    }
}