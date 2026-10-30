#  program to find the sum and average of N numbers using for loop

N = int(input("Enter a number: "))
sum = 0 
for i in range(N):
    num = float(input("Enter a number: "))
    sum = sum + num

average = sum / N

print(f"Sum of {N} numbers is {sum}")
print(f"Average of {N} numbers (sum {sum}) is {average}")