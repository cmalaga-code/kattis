def input_integer():
    time = input()
    return time.split(" ")

def conversion(time):
    if int(time[1]) < 45:
        if int(time[0]) == 0:
            remainder = 45 - int(time[1])
            new_hour = 23
            new_minute = 60 - remainder
            print(new_hour, new_minute)
        else:
            remainder = 45 - int(time[1])
            new_hour = int(time[0]) - 1
            new_minute = 60 - remainder
            print(new_hour, new_minute)
    else:
        new_minute = int(time[1]) - 45
        print(time[0], new_minute)

if __name__ == "__main__":
    t = input_integer()
    conversion(t)
