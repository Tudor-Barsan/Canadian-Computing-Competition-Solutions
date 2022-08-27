time = input()
time = time.replace(":", "")

if time[0] == "0":
    time = int(time[1]) * 60 + int(time[2]) * 10 + int(time[3])
else:
    time = int(time[:2]) * 60 + int(time[2]) * 10 + int(time[3])

i = 120
time = int(time)

while i > 0:
    time = time % 1440
    if 420 < time < 600 or 900 < time < 1140:
        i -= 0.5
    else:
        i -= 1
    time += 1

hour = int(time / 60)
minute = time % 60

if hour > 9 and minute == 0:
    print(f"{hour}:{minute}0")

elif hour > 9 and minute != 0:
    print(f"{hour}:{minute}")

elif hour < 9 and minute == 0:
    print(f"0{hour}:{minute}0")

else:
    print(f"0{hour}:{minute}")