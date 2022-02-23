#accept string name from the user and display characters, that are present at an even index
str = input("Enter a string:")
index = 0

while(index < len(str)):
      print(str[index],end = '')

      index = index + 2
