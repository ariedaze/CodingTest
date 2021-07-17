func solution(_ s:String) -> String {
    
    let result = s.sorted(by: >)
    var answer : String = ""
    
    for i in result {
        //swift에서는 문자열을 더해줄때 String으로 감싸서 더해줘야한다.
        answer += String(i)
    }
    
    return answer
