s=int(input("enter the size:"))
for i in range(s):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()

for i in range(s):
    for j in range(s-i-1):
        print(chr(65+j),end="")
    print()

