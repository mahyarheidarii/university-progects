code = "0025096583"  
vector = []

for digit in code:
    num = int(digit)
    if num not in vector:
        vector.append(num)

print(vector)