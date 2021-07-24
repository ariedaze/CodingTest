func solution(_ s:String) -> String {
    var stringSort = s.sorted(by: >)
    var answer: String = ""

    for i in stringSort {
        answer += String(i)
    }
    return answer
}