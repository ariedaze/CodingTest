import kotlin.math.*

class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        var check = DoubleArray(N+1)
        var length: Int = stages.size
        for (i in 1..N) {
            if (length > 0) {
                check[i] = stages.count{it == i}.toDouble() / length
                length -= stages.count{it == i}
            }
        }
        check[0] = -1.0
        for (i in 1..N) {
            val idx = check.indexOf(check.max()!!)
            answer.add(idx)
            check[idx] = -1.0
        }
        return answer.toIntArray()
    }
}