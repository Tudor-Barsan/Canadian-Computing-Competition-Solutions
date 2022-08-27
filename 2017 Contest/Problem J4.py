def arithmetic_time(time):
    if len(str(time)) == 3:
        if int(str(time)[-1]) - int(str(time)[-2]) == int(str(time)[-2]) - int(str(time)[-3]):
            return True
        else:
            return False
    else:
        if int(str(time)[-1]) - int(str(time)[-2]) == int(str(time)[-2]) - int(str(time)[-3]) == int(str(time)[-3]) - int(str(time)[-4]):
            return True
        else:
            return False


def time_fix(time):
    if int(str(time)[-2]) == 6:
        time += 40
    if int(str(time)[1]) == 3 and len(str(time)) == 4:
        time = 100

    return time


seconds = int(input())
d = seconds % 720
time = 1200
count = 31 * (int(seconds/720))

for i in range(d):
    time += 1
    time = time_fix(time)
    if arithmetic_time(time):
        count += 1

print(count)