#finance_calculators.py
#import from the math libary 

import math

#The program welcomes the user with a message
#the program gives the user a brief description of what service they offer and what they can calculate
#the program request information the user that it will use to calculate what the user wants to calculate
#the answer is capitalized so that no matter what case the user uses the program will excute 

print("Thank you for choosing our financial institution")

print("\n")

print("Please see which type of service you would like to calculate between the two below:\n \n Investment   -To calculate the amount of interest you will earn your investment\n Bond         -To calculate the amount you will have to pay on a home loan")

print("\n")

answer= input("Please enter the the type of service you would like to calculate :")

answer_cap= (answer.capitalize())


#The if statement is executed if the user enters the word investment
#the program request user for additional info based on the choice they made
if answer_cap=="Investment":
    
    print("You have selected to calculate the investment option ")

    print("\n")

    amount_dep= float(input("Please enter the amount you would like to deposit for your investment :"))
    
    rate= float(input("Please enter the interest rate you would like :"))

    num_years= int(input("Please enter the number of years you would like to invest for :"))

    interest1= input("Would you like compound or simple inetrest :")

    interest2= (interest1.capitalize())

#if statment is executed when user chooses the simple interest
#calculations of the simple interest based on the information given by user using the given formula 
#calculations for differece it is 20 years at 8%   using the given formula  
#print a message to the user 
#second if statment is to make sure the difference of the simple interest stays postive by multipling by -1 or stay as is   
    if interest2=="Simple":

        total_simple= round(amount_dep*(1+rate/100*num_years ),2)

        simple_amount= round((total_simple-amount_dep),2)

        difference_simple= round(amount_dep*(1+8/100*20),2)

        
        print("\n")
        
        print("The simple interest amount for a {} year/s invesment at {}% is R{} and the total all together is R{}".format(num_years,rate,simple_amount,total_simple))

        if total_simple>difference_simple:

            total_difference1= round((((total_simple-difference_simple)*-1),2))

            print("If you were to invest for 20 years at 8%,the difference would be R{}".format(total_difference1))

        elif difference_simple>total_simple:

            total_difference1= round((difference_simple-total_simple),2)

            print("If you were to invest for 20 years at 8%,the difference would be R{}".format(total_difference1))


#if statment is executed when user chooses the compund interest
#calculations of the compound interest based on the information given by user using the given formula 
#calculations for differece it is 20 years at 8% using the given formula    
#print a message to the user 
#second if statment is to make sure the difference of the simple interest stays postive by multipling by -1  or stay as it is           
        
    elif interest2=="Compound":

        total_compund= round(amount_dep*(pow((1+rate/100), num_years)),2)

        compound_amount= round((total_compund-amount_dep),2)

        difference_compound= round(amount_dep*(pow((1+8/100),20)),2)

        print("\n")
        
        print("The compound interest amount for a {} year/s invesment at {}% is R{} and the total all together is R{}".format(num_years,rate,compound_amount,total_compund))

        if total_compund>difference_compound:

            total_difference2= round(((total_compund-difference_compound)*-1),2)

            print("If you were to invest for 20 years at 8%,the difference would be R{}".format(total_difference2))

        elif difference_compound>total_compund:

            total_difference2= round((difference_compound-total_compund),2)

            print("If you were to invest for 20 years at 8%,the difference would be R{}".format(total_difference2))

#if the user did not select between simple and compound the this message will be displayed
    
    else:
        
        print("you have not selected the given choices")
        
#this elif is executed when the user choose the bond option instead of the investment option
#the program request user to enter infomation
   
elif answer_cap=="Bond":
    
    print("You have selected to calculate the bond option ")

    print("\n")
    
    present_value= float(input("Please enter the present value of your house: "))

    rate_interest=(input("Please enter the interest rate: "))

    rate_interest2= float(rate_interest)

    num_months= int(input("Please enter the number of months you plan to repay the loan: "))

#calculations for the monthly payments based on the given data from the user using the given formula
#print a message for the user
    
    monthly_installments=round((present_value*(rate_interest2/1200))/(1-(1+(rate_interest2/1200))**(num_months*-1)),2)
    
    print("\n")
    
    print("Your monthly payments will be R{}".format(monthly_installments))
    
#if the user did not choose  between bond or investment  then a error message will appear 

else:
    
    print("You have not seleted from the choice above")




