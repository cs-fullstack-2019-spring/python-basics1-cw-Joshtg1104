def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()

#### Problem 1:
# Create a function with two variables.
# One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.

def problem1():
    greeting = "My name is: "
    myName = "Joshua Graham"
    print(greeting + myName)


#### Problem 2:
# Create a function to ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.

def problem2():
    extraCredit = int(input("Enter earned extra credit points"))
    if(extraCredit<5):
        print("That's not enough extra credit.")
    elif(extraCredit>20):
        print("That's too much extra credit.")

#### Problem 3:
# Create a function to ask a user to enter a password.
# Enter a password.
# Ask user to reenter password.
# Check to see if they are correct.

def problem3():
    passWord = input("Please enter new password")
    confirm = input("Re-enter password")
    if(confirm != passWord):
        print("Passwords Do Not Match!")
    elif(confirm == passWord):
        print("New Password Confirm!")

#### Problem 4:
# Create a function to ask for two card numbers.
# If it equals 21 print BLACKJACK!,
# if it’s greater than 21 print BUST!,
# if it’s less than 21 print “The total is [THE TOTAL]”

def problem4():
    card1 = int(input("Enter a number"))
    card2 = int(input("Enter another number"))
    total = card1 + card2
    if(total == 21):
        print("BLACKJACK!!")
    elif(total > 21):
        print("BUST!!")
    else:
        print("The total is " + str(total))


if __name__ == '__main__':
    main()
