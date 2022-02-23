#Check whether the given num is palindrome or not
num = int(input("Enter a number:"))
temp = num
reverse = 0

while(num>0):
    dig = num%10
    reverse = reverse*10+dig
    num = num//10
if (temp == reverse):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
    
