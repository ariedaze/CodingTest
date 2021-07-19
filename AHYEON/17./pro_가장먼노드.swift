import Foundation

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    var graph: [Int: [Int]] = [:]

    func connect(key: Int, value: Int) {
        if graph.keys.contains(key) {
            graph[key]?.append(value)
        } else {
            graph[key] = [value]
        }
    }

    for e in edge {
        connect(key: e[0], value: e[1])
        connect(key: e[1], value: e[0])
    }

    var Q: [(Int, Int)] = []
    var answer: [(Int, Int)] = []

    var visited: [Bool] = Array(repeating: false, count: graph.keys.count)

    func bfs(key: Int, depth: Int) {
        for node in graph[key]! {
            if visited[node-1] {
                continue
            }
            visited[node-1] = true
            answer.append((node, depth))
            Q.append((node, depth))
            }
        }
        Q.append((1,0))
        visited[0] = true
        while !Q.isEmpty {
            let node = Q.removeFirst()
            bfs(key: node.0, depth: node.1+1)
        }
        let maxNum = answer.max {$0.1 < $1.1}.map {$0.1}
        var count = 0
        for node in answer {
            if maxNum == node.1 {
            count += 1
            }
        }
        return count

}



