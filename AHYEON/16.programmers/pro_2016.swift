let dayOfWeek = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

func solution(_ a:Int, _ b:Int) -> String {
    var numCount: Int = 3 + b

    for month in 1..<a {
        switch month {
            case 1, 3, 5, 7, 8, 10, 12:
                numCount += 31
            case 2:
                numCount += 29
            default:
                numCount += 30
        }
    }

    return dayOfWeek[numCount%7]
}