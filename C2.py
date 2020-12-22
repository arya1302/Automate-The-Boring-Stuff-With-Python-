# Practice Questions

# 1. What are the two values of the Boolean data type? How do you write them?

#   Ans:
#          true and false,
#          Can be written as  True , False        



#  2. What are the three Boolean operators?

#   Ans :  and , or , not 



# 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

# Ans

# and

#   T T - T
#   T F - F
#   F T - F
#   F F - F
#

#  or
#
#    T T  -T
#    T F  -T
#    F T  -F
#    F F  -F


#   not

#    T - F
#    F - T




#4. What do the following expressions evaluate to?
#(5 > 4) and (3 == 5)             # False
#not (5 > 4)                      #False 
#(5 > 4) or (3 == 5)               #True
#not ((5 > 4) or (3 == 5))          #False
#(True and True) and (True == False) #False
#(not False) or (not True)            #True




# 5. What are the six comparison operators?

# Ans :

# ==       Equal to
# !=     Not equal to
# <    Less than
# >     Greater than
# <=     Less than or equal to
#>=    Greater than or equal to



# 6. What is the difference between the equal to operator and the assignment operator?

# Ans  :  Equal to operator checks the equality and is a comparison operator,
#     whereas assignment operator is used to store or assign a value to a variable (eg spam = 10)




#7. Explain what a condition is and where you would use one.

#   Ans: condition is an expression which evaluates to a Boolean value . Flow control statements use condition to decide upon what needs to be done 



#8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')


#1. print('eggs')
#2. print('bacon')
#3. print('ham') , print('spam') ,print('spam')



#9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam

spam = 2
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else :
    print( 'Greetings!')


    
#10. What keys can you press if your program is stuck in an infinite loop?

 # Ans:        Ctrl+C.

 

# 11. What is the difference between break and continue?

#Ans : If the execution reaches a break statement, it immediately exits the loop’s clause whereas if the execution reaches a continue statement,
#   the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition




#12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

#Ans   : range(10) - range from 0 to 9
#       range(0,10) - range from 0 to 9
#   :   range(0,10,1)- start at 0 and increase the variable by 1



#13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

#using for loop
for i in range (1 , 11):
 print(i) 

#using while loop
 i =1
while i < 11 :
 print(i)
 i =i+1


#14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
 #Ans :  By using spam.bacon()
