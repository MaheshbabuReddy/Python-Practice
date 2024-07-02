stones = "z"
jawels ="ZZZ"
count = 0
for i in range(len(jawels)):
    if jawels[i] in stones:
        count += 1
print(count)