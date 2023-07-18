s=int(input("enter the size:"))
for i in range(s):
    for j in range(1,s-i):
        print(" ",end="")
    for k in range(i+1):
        print(chr(65+k),end="")
    print()
