import kotlin.math.*

class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        val check = n.toString(3).split("")
        for ((idx,num) in check.withIndex()) {
            if (num != "" && num != "0") {
                answer += ((3.0).pow(idx-1)).toInt()*num.toInt()
            }
        }
        return answer
    }
}