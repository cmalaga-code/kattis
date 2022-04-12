def sticker_fit_test(laptop_width, laptop_height, sticker_width, sticker_height):
    if (laptop_width - sticker_width) >= 2 and (laptop_height - sticker_height) >= 2:
        return 1
    else:
        return 0
    

if __name__ == "__main__":
    _ = input().split(" ")
    laptop_width = int(_[0])
    laptop_height = int(_[1])
    sticker_width = int(_[2])
    sticker_height = int(_[3])
    solution = sticker_fit_test(laptop_width, laptop_height, sticker_width, sticker_height)
    print(solution)