def compare(x, y):
    if x > y:
        return 1
    else:
        return 0

if __name__ == "__main__":
    number1, number2 = input().split(" ")
    solution = compare(number1, number2)
    print(solution)