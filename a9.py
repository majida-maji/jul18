s=int(input("enter the size:"))
for i in range(s):
    for j in range(s-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print(chr(65+j),end="")
    print()

for i in range(s-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(2*(s-i-1)-1):
        print(chr(65+j),end="")
    print()

