routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

routes.sort(key=lambda x: x[1])
print(routes)

result = 0
while routes:
    start, end = routes.pop(0)
    result += 1
    cut = True
    while cut:
        for route in routes:
            if route[0] <= end:
                routes.remove(route)
                break
        else:
            cut = False
print(result)
