from copy import deepcopy
options = [["*","+","-"],["*","-","+"],["+","*","-"],["+","-","*"],["-","+","*"],["-", "*", "+"]]
expression = "50*6-3*2"
origin_nums = list(map(int, expression.replace("*", "+").replace("-","+").split("+")))
origin_logics = [ ]
results = []

def go_logic(exp, x, y):
    if exp == "+":
        return x+y
    elif exp == "-":
        return x-y
    else:
        return x*y

for i in range(len(expression)):
    if expression[i] == "*" or expression[i] == "-" or expression[i] == "+":
        origin_logics.append(expression[i])
for option in options:
    nums = deepcopy(origin_nums)
    logics = deepcopy(origin_logics)
    for log in option:
        while log in logics:
            for idx, logic in enumerate(logics):
                if log == logic:
                    nums.insert(idx, go_logic(logics.pop(idx),nums.pop(idx),nums.pop(idx)))
                    break
    results.append(abs(nums[0]))
print(max(results))

