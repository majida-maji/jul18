s=int(input("enter the size:"))
for i in range(s):
    for j in range(s-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print(chr(65+k),end="")
    print()
