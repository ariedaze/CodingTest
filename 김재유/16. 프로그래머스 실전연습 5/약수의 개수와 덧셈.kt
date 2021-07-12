class Solution {
    fun solution(left: Int, right: Int): Int {
        val doublecheck = IntArray(32, {i -> i*i})
        var answer: Int = 0
        for (number in left..right) {
            if (number in doublecheck) {
                answer -= number
            } else {
                answer += number
            }
        }
        return answer
    }
}