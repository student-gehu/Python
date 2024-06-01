"""f1=input("enter the string:")
file=open("f1.txt","r")
c=0
while True:
    char=file.read(1)
    if not char:
        break
    if not (char>='a' and char <='z')and not(char>='A' and char<='Z'):
        c=c+1
print(c)
file.close()"""

# Get the string input from the user
f1 = input("Enter the string:")

# Write the input string to f1.txt
with open("f1.txt", "w") as file:
    file.write(f1)

# Initialize the non-alphabetic character count
c = 0

# Open the file in read mode to count non-alphabetic characters
with open("f1.txt", "r") as file:
    while True:
        char = file.read(1)
        if not char:
            break
        if not (char >= 'a' and char <= 'z') and not (char >= 'A' and char <= 'Z'):
            c += 1

# Print the count of non-alphabetic characters
print(c)

