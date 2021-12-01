a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("The first number is the biggest")
    input()
if b > a and b > c:
    print("The second number is the biggest")
    input()
if c > b and c > a:
    print("The third number is the biggest")
    input()
if a == b and a == c:
    print("All of the numbers are equal")
    input()
