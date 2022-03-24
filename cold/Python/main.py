def below_zero(temp):
    below_zero_count = 0
    for element in temp:
        if int(element) < 0:
            below_zero_count += 1
        else:
            continue
    return below_zero_count


number_of_temperatures = input()
temperature_list = input().split(" ")
solution = below_zero(temperature_list)
print(solution)
