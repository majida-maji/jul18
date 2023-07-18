s=int(input("enter the size:"))
count=0
for i in range(s):
    for j in range(s):
        print(chr(65+count),end="")
        count+=1
    print()
