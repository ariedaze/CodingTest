import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    let n: Int = n
    let lost: [Int] = lost
    let reserve: [Int] = reserve
    var student: [Int] = [Int](repeating: 1, count: n)
    // 0: 없음 2: 여유있음

    for l in lost {
        student[l-1] = student[l-1] - 1
    }

    for r in reserve {
        student[r-1] = student[r-1] + 1
    }

    for (index, value) in student.enumerated(){
        if value == 0 {
            if (index > 0 && student[index - 1] == 2){
                student[index - 1] -= 1
                student[index] += 1
            }else if (index < student.count - 1) && student[index + 1] == 2{
                student[index + 1] -= 1
                student[index] += 1
            }
        }
    }

    var result = student.filter{($0 >= 1)}.count

    return result
}