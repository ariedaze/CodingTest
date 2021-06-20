func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
    var A = a
    var B = b
    var round = 0

    while A != B {

        if A%2 == 1 {
            A = (A + 1)/2
        }else{
            A = A/2
        }

        if B%2 == 1 {
            B = (B + 1)/2
        }else{
           B = B/2
        }


        round += 1
    }
    return round
}
