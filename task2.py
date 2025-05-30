#Uses a for loop to iterate over numbers from 1 to 50.
num = range(1, 51)
for num in range(51):
    print(num)


#calculate the sum of all integer numbers from 1 to 50
# Initialize sum to 0
sum = 0

# Use for loop with range to iterate from 1 to 50
for num in range(1, 51):  # range(1, 51) goes from 1 to 50
    sum += num  # Add each number to the sum

# Display the final sum
print("The sum of numbers from 1 to 50 is:", sum)