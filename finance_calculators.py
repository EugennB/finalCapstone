import math

print("Please choose from the following 2 options what you would like to calculate:")
print("-> investment - to calculate the amount of interest you'll earn on your investment")
print("-> bond - to calculate the amount you'll have to pay on a home loan")
print("")

def correct_answer():
    answer = input("Type'investment' or 'bond' from the menu above to proceed:\n>")

    if answer.lower() == "investment":
        
        while True:
                try: 
                        P = float(input("Enter the amount of money that you are depositing in pounds.\n>"))
                        break
                except ValueError:
                        print("Oops! I cannot use that. Please only enter a number!")
        while True:
                try: 
                        interest = float(input("Enter your interest rate.\n>"))
                        break
                except ValueError:
                        print("Oops! I cannot use that. Please only enter a number!")
        while True:
                try: 
                        t = float(input("Enter how many years you plan on investing for.\n>"))
                        break
                except ValueError:
                        print("Oops! I cannot use that. Please only enter a number!")
        r = interest/100
        var = True
        while var:
                i = input("Do you want simple or compound interest? Please type your answer.\n>")
                if i.lower() == "simple":
                        var = False
                        A = P*(1 + r*t)
                        print("The total amount you will earn after " + str(t) + " years at an interest rate of " + str(interest) + "% is " + str(A) + " pounds.")
                elif i.lower() == "compound":
                        var = False
                        A = P * math.pow((1+r),t)
                        print("The total amount you will earn after " + str(t) + " years at an interest rate of " + str(interest) + "% is " + str(A) + "pounds.")
                else:
                        var = True
                        print("Oops! I cannot use that. Please only type 'simple' or 'compound'.")  

    elif answer.lower() == "bond":
                
        while True:
                try: 
                        P = float(input("Enter the present value of the house in pounds.\n>"))   
                        break
                except ValueError:
                        print("Oops! I cannot use that. Please only enter a number!")
        while True:
                try: 
                        interest = float(input("Enter your anual interest rate.\n>"))
                        break
                except ValueError:
                        print("Oops! I cannot use that. Please only enter a number!")
        while True:
                try: 
                        n = float(input("In how many months do you wish to repay your bond?\n>"))
                        break
                except ValueError:
                        print("Oops! I cannot use that. Please only enter a number!")
        i = interest/100/12
        repayment = (i * P)/(1 - (1 + i)**(-n))
        print("The amount you will have to repay each month is " + str(repayment) + " pounds.")
    else:
        print("Sorry. You can only choose one of the 2 options. Please try again.")
        return correct_answer()
correct_answer()

'''I've uploaded the initial file onto dropbox on 31 March. Given the fact that it wasn't reviewed yet and the deadline did not pass,
I've decided to add some defensive coding and comments today (3rd April).
If it is an issue I can reupload the initial file.'''