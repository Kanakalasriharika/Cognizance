#print the pattern
r = int(input("Enter number of rows:"))
for p in range (r) :
    for q in range(r-p-1) :
        print(" ",end="")
    for q in range(p+1):
        print("*",end=" ")
    print()
    
