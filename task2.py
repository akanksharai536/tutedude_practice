
"""num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")  """


total_sum = 0
for num in range(1,51):
    if num >= 1:
        total_sum += num
    else:
        total_sum = total_sum
print(f"The sum of numbers from 1 to 50 is: {total_sum}")