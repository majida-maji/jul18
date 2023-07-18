s=int(input("enter the size:"))
for i in range(s):
    for j in range(i+1):
        print(chr(j+65),end="")
    print()
