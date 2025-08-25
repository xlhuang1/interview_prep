# Given an array temps where temps[i] is the daily temperature,
# return an array wait where wait[i] is the number of days after day i you must wait until a warmer temperature.
# If there’s no future day for which this is possible, set wait[i] = 0.

def daily_temps(temps):
    wait = [0] * len(temps)
    stack = []      # stack of Temps that is index with temps strictly decreasing from bottom to top (largest temps at bottom, smallest at top)

    for i, temp in enumerate(temps):
        while stack:
            # resolve temps from earlier days based on current day's temp
            if temp > temps[stack[-1]]:
                j = stack.pop()
                wait[j] = i-j
            else:
                break
        stack.append(i)
    return wait

print(daily_temps([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(daily_temps([30,40,50,60]))              # [1,1,1,0]