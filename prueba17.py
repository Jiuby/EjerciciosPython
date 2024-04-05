# https://www.codeabbey.com/index/task_view/fahrenheit-celsius

# Fahrenheit to Celsius

data = list(map(int, input().split()))

N = data.pop(0)

results = []

for i in range(N):
    celsius = (data[i] - 32) * 5 / 9
    results.append(int(celsius + 0.5 * (1 if celsius > 0 else -1)))

print(' '.join(map(str, results)))