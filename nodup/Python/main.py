def test_if_duplicate_in_string(x):
    _ = x.split(" ")
    beginning_length = len(_)
    no_duplicate_length = len(set(_))

    if beginning_length > no_duplicate_length:
        return "no"
    else:
        return "yes"

if __name__ == "__main__":
    input_string = input()
    solution = test_if_duplicate_in_string(input_string)
    print(solution)