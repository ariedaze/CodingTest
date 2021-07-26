class Solution {
    fun solution(key: Array<IntArray>, lock: Array<IntArray>): Boolean {
        var curKey = key
        fun rotate() {
            curKey = Array(curKey.size) {
                    i -> IntArray(curKey.size) {
                    j -> curKey[curKey.size - 1 - j][i]
            }
            }
        }

        fun check(k_y: Int, k_x: Int): Boolean {
            for (y in 0 until lock.size) {
                for (x in 0 until lock.size) {
                    val isOutOfKey = 0 > y - k_y || y - k_y >= curKey.size || 0 > x - k_x || x - k_x >= curKey.size
                    if (lock[y][x] == 0 && (isOutOfKey || curKey[y - k_y][x - k_x] == 0)) {
                        return false
                    }

                    if (lock[y][x] == 1 && !isOutOfKey && curKey[y - k_y][x - k_x] == 1) {
                        return false
                    }
                }
            }
            return true
        }

        for (r in 0..3) {
            for (y in -lock.size + 1 until lock.size) {
                for (x in -lock.size + 1 until lock.size) {
                    if (check(y, x)) {
                        return true
                    }
                }
            }
            rotate()
        }

        return false
    }
}