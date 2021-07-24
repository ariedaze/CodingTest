class Solution {
    fun solution(n: Int, results: Array<IntArray>): Int {
        val winnings = Array(n + 1) { Array(n + 1) { 0 } }

        for (result in results) {
            winnings[result[0]][result[1]] = 1
            winnings[result[1]][result[0]] = -1
        }

        for (k in 1..n) {
            for (i in 1..n) {
                for (j in 1..n) {
                    if (winnings[i][j] != 0) { continue }

                    if (winnings[i][k] == winnings[k][j]) {
                        winnings[i][j] = winnings[i][k]
                    }
                }
            }
        }

        return winnings.filter { winning -> winning.count { w -> w != 0 } == n - 1 }.size
    }
}