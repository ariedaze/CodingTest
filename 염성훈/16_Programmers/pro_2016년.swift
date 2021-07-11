
func solution(_ a:Int, _ b:Int) -> String {
    
    let days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    let months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    var totalDays = 5
    for i in 0..<a-1 {
        totalDays += months[i]
    }
    // 인덱스는 1을 빼고 계산해야한다.
    totalDays += b-1
    
    return days[totalDays%7]
}
