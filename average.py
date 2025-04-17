import sys

total = 0
count = 0

for line in sys.stdin:
    try:
        num = float(line.strip())
        total += num
        count += 1
    except:
        pass

if count > 0:
    print("Average:", total / count)