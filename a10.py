s=int(input("enter the size:"))
for i in range(s):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(s-i)-1):
        print(chr(65+j),end="")
    print()



