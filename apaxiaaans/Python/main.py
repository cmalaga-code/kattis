def compact(x):
    cache_letter = ""
    new_name = ""
    for _ in x:
        if _ == cache_letter:
            continue
        else:
            new_name += _
        cache_letter = _
    return new_name

if __name__ == "__main__":
    name = list(input())
    solution = compact(name)
    print(solution)