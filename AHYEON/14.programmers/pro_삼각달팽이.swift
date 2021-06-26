import Foundation

enum Direction {
    case down
    case up
    case right
}


func solution(_ n:Int) -> [Int] {

  var direction: Direction = .down
  var array: [[Int]] = [] // 달팽이 채우기를 진행할 배열
  var sum = 0
  var oneline = n - 1 == 0 ? 1 : n - 1 // 각 방향당 저장할 숫자의 개수
  var count = 1
  var value = 0
  var result: [Int] = []

  for i in 0..<n {
    array.append([Int](repeating: 0, count: i+1))
    sum += i + 1
  }

  // 각 방향별로 배열에 값을 채워준다
  repeat {
    switch direction {
    case .down:
      for i in 0..<oneline {
        array[i+(value*2)][value] = count
        count += 1
      }
      direction = .right

    case .right:
      for i in 0..<oneline {
        array[n-1-value][i+value] = count
        count += 1
      }
      direction = .up

    case .up:
      for i in value..<oneline+value {
        array[n-1-i][n-1-i-value] = count
        count += 1
      }
      direction = .down
      oneline = oneline - 3 == 0 ? 1 : oneline - 3
      value += 1
    }
  } while count <= sum

  for arr in array {
    for i in arr {
      result.append(i)
    }
  }

  return result
}