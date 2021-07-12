class Solution {
    fun solution(a: Int, b: Int): String {
        var answer = ""
        val days = listOf("THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED")
        val months = listOf(31,29,31,30,31,30,31,31,30,31,30,31)
        var check : Int = b
        for (i in 0..a-2) {
            check += months[i]
        }
        answer = days[check%7]
        return answer
    }
}