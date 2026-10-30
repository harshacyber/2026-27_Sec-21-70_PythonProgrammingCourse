# program to print the multiplication table of a number using for loop 

N = int(input("Enter a number: "))

for i in range(1, 11):
    product = N * i
    print(f"{N} x {i} = {product}")

# program to print the multiplication table of a number using while loop 3
 
N = int(input("Enter a number: "))

i = 1

while i <= 10:

    product = N * i
    print(f"{N} x {i} = {product}")

    i += 1 