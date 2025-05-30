# Assignment-No.---2

Module2 : Control structure in python

 ---- in task 1 -----
Input Section:

This is a beginner-friendly Python script that helps you find out whether a number you enter is even or odd.

What Does This Code Do?
Takes an integer input from the user.

Checks if the number is even or odd using a simple mathematical condition.

Displays the result to the user in a clear message.

How Does It Work?
User Input:
The script asks you to enter any integer (positive, negative, or zero).

The code uses the modulus operator % to find the remainder when your number is divided by 2.

The % symbol is called the modulus operator in Python.

It gives the remainder when one number is divided by another.

----------Second Task-----------
First Part:
Uses a for loop to print every number from 0 to 50 (inclusive).

Firstly num variable is taken which takes range(51) which generates a sequence of numbers starting from  up to 50 (it stops before 51).
Then it prints or displays these numbers starting from 1 upto 50 as it takes only upto 50 and leave 51.

range(1, 51):

This creates a sequence of numbers starting from 1 up to (but not including) 51.

So it generates: 1, 2, 3, ..., 49, 50.

for num in range(1, 51):

This loop goes through each number in the sequence one by one.

Each time, the variable num takes the next value in the sequence.

sum += num:

This is a shortcut for sum = sum + num.

It adds the current num to the running total stored in sum.

Example: If sum is 6 and num is 4, then after this line, sum becomes 10.

After the Loop:

Once all numbers from 1 to 50 have been added, sum contains the total sum of these numbers.

print("The sum of numbers from 1 to 50 is:", sum):

This prints out the final result.

Why Does This Work?
The loop ensures that every number from 1 to 50 is added to sum.
