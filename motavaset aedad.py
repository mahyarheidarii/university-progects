import random

with open("data.txt", "w") as f:
    for _ in range(1000):
        f.write(f"{random.random()}\n")

print("File 'data.txt' with 1000 random numbers has been created.")

numbers = []
with open("data.txt", "r") as f:
    for line in f:
        try:
            num = float(line.strip())
            numbers.append(num)
        except ValueError:
            print(f"Invalid line skipped: {line.strip()}")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Average of {len(numbers)} numbers: {average}")
else:
    print("No valid numbers found in the file.")