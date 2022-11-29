# Ask the user to input 3 numbers and you have to print average of 3 numbers using string formatting.
# Bonus:- Try to take all 3 comma seperated inputs in one line.

# SOLUTION:-

num1, num2, num3 = input("enter three comma seperated numbers:- ").split(",")
print(f"Average is {(int(num1)+int(num2)+int(num3))/3}")