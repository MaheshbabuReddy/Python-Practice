f=open("C://temp/java/myfile1.txt","w+")
Sentence="I saw the Sea in saw world in saw state"
word="saw"
count=0
s=Sentence.split()
for l in s:
    if l==word:
        count+=1
        c=str(count)
f.writelines(f"It is count of {word}:{c}")
f.close()

