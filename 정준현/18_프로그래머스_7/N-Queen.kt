class Solution {
    fun solution(n: Int): Int {
        var answer = 0
        val x_visited = Array(n + 1) { 0 }
        val y_visited = Array(n + 1) { 0 }
        val d_1_visited = Array(2 * n) { 0 }
        val d_2_visited = Array(2 * n) { 0 }

        fun dfs(y: Int) {
            if (y >= n) {
                answer += 1
                return
            }

            for (x in 0 until n) {
                if (x_visited[x] == 0 && y_visited[y] == 0 && d_1_visited[y + x] == 0 && d_2_visited[y - x + (                    n - 1)] == 0) {
                    x_visited[x] += 1
                    y_visited[y] += 1
                    d_1_visited[y + x] += 1
                    d_2_visited[y - x + (n - 1)] += 1
                    dfs(y + 1)
                    x_visited[x] -= 1
                    y_visited[y] -= 1
                    d_1_visited[y + x] -= 1
                    d_2_visited[y - x + (n - 1)] -= 1
                }
            }
        }

        dfs(0)

        return answer
    }
}