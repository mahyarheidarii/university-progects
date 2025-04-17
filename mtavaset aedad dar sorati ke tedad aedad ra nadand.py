total = 0.0
count = 0

with open("data.txt", "r") as f:
    for line in f:
        try:
            num = float(line.strip())
            total += num
            count += 1
        except ValueError:
            print(f"Invalid line skipped: {line.strip()}")

if count > 0:
    average = total / count
    print(f"Average of {count} numbers: {average}")
else:
    print("No valid numbers found in the file.")