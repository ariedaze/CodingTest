import java.util.*

class Solution {
    fun solution(operations: Array<String>): IntArray {
        val minQueue = PriorityQueue<Int>()
        val maxQueue = PriorityQueue<Int>(Collections.reverseOrder())

        for (oper in operations) {
            if (oper[0] == 'I') {
                val num = oper.slice(2 until oper.length).toInt()
                minQueue.add(num)
                maxQueue.add(num)
            } else {
                if (oper[2] == '-') {
                    maxQueue.remove(minQueue.poll())
                } else {
                    minQueue.remove(maxQueue.poll())
                }
            }
        }

        return intArrayOf(maxQueue.poll() ?: 0, minQueue.poll() ?: 0)
    }
}