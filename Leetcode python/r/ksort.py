arr =[2,4,21,23,1,12]
k = 3
rev = arr[::-1]
chuncks = []
print(rev)
for i in range(0,len(rev),k):
    result = rev[i:i+k]
    if result:
        chuncks.append(result) 
print(chuncks)
for i in range(len(chuncks)-1):
     print(chuncks[i][::-1]+chuncks[i+1][::-1])



#Other method   
arr = [2, 4, 21, 23, 1, 12]
k = 2

chunks = [arr[::-1][i:i+k] for i in range(0, len(arr), k)]

# Concatenate reversed chunks pairwise and print
results = []
for i in range(len(chunks) - 1):
    concatenated_chunks = chunks[i][::-1] + chunks[i + 1][::-1]
    results.append(concatenated_chunks)

print("Concatenated reversed chunks:", results)
