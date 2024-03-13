#Write a program to determine if a person is eligible for a discount on a movie ticket based on their age and whether they are a student or not.Follow these steps:
#Ask the user to input their age.
Giveage=int(input("Enter your age bbg:"))
is_student= input("Are you a student?(yes/no):").lower()

if is_student == "yes":
    is_student == True
elif is_student == "no":
    is_student == False
else:
    print (" Invalid input. please enter 'yes' or 'no'.") 
    return

#Check eligibility for a discount using logical operators
if (age< 12 or >=11) or (is_student and age<= 12)
    print(" You are eligible for a discount on the movie ticket")
else:
    print("You are not eligible for a discount on the movie ticket.")  
    return


