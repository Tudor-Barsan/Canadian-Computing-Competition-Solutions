import math

#determine max value for elements between start and end inclusive
def maxim(start, end):
    global a
    max1 = -1
    for i in range(start, end + 1):
        if a[i] > max1:
            max1 = a[i]
    return max1


def MaxScore(n, days, minday):
    global a
    global k
    global dp

    res = dp[n][days][minday]
    if res != -1:
        return res

    if days == 1:
        res = maxim(0, n-1)
        dp[n][days][minday] = res
        return res
    if minday == k:
        scoreday = maxim(n - k, n - 1)
        score_previous_days = MaxScore(n - k, days - 1, k)
        res = scoreday + score_previous_days
        dp[n][days][minday] = res
        return res

    max1 = -1
    for no_attract in range(minday, k + 1):
        scoreday = maxim(n-no_attract, n - 1)
        score_previous_days = MaxScore(n - no_attract, days - 1, minday + k - no_attract)
        total = scoreday + score_previous_days
        if total > max1:
            max1 = total

    dp[n][days][minday] = max1
    return max1


n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

days = math.ceil(n/k)
minperday = n % k

dp = [[[-1 for i in range(0, k + 1)] for j in range(0, days + 1)] for t in range(0, n + 1)]

print(MaxScore(n, days, minperday))
