n=int(input("enter the no:"))
for i in range(n):
    for j in range(n-i-1):
        print("",end="")
    for j in range(2*i+1):
        print(j+1,end="")
    print()

for i in range(n-1):
    for j in range(i+1):
        print("",end="")
    for j in range(2*(n-i-1)):
        print(j+1,end="")
    print()
