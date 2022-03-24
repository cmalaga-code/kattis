def max_combination(n, t, m):
    return (n*t)*m

eye, nose, mouth = input().split(" ")
solution = max_combination(int(eye), int(nose), int(mouth))
print(solution)