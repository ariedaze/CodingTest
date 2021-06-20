import Foundation

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    var cnt = 0
    for s in skill_trees {
        var currentSkill = ""
        for c in s {
            if skill.contains(c) {
                currentSkill += c.description
            }
        }
        
        if skill.hasPrefix(currentSkill) {
            cnt += 1
        }
    }
    return cnt
}