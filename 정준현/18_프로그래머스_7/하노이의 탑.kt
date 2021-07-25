class Solution {
    fun solution(n: Int): Array<IntArray> {
        var answer = mutableListOf<IntArray>()
        fun hanoi(num: Int, start: Int, end: Int, via: Int) {
            if (num == 1) {
                answer.add(intArrayOf(start, end))
                return
            }

            hanoi(num - 1, start, via, end)
            answer.add(intArrayOf(start, end))
            hanoi(num - 1, via, end, start)
        }

        hanoi(n, 1, 3, 2)

        return answer.toTypedArray()
    }
}