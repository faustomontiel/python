#def sum_of_integers(n):
#  if n < 1:
#    return 0
#
#
#  i = 1
#  sum = 0
#  while i <= n:
#    sum = sum + i
#    i = i + 1
#
#  return sum
#
#
#print(sum_of_integers(3))  # should print 6
#print(sum_of_integers(4))  # should print 10
#print(sum_of_integers(5))  # should print 15


#friends = ['Taylor', 'Alex', 'Pat', 'Eli']
#for friend in friends:
#    print("Hi " + friend)
#
#bill = 47.28 # Assign "bill" variable with bill amount
#tip = bill * 0.15 # Multiply by stated tip rate 
#total = bill + tip # Sum the "total" of the "bill" and "tip"
#share = total / 2 # Divide "total" by number of friends dining
#print("Each person needs to pay: " + str(share)) # Enter the required string and "share" 
## Hint: Remember to convert incompatible data types
#
#def greeting(name, department):
#    print("Welcome, " + name)
#    print("You are part of " + department)
#    
#greeting("Blake", "Software engineering")
#greeting("Ellis", "Software engineering")
#
#def area_triangle(base, height):
#    return base*height/2
#area_a = area_triangle(5,4)
#area_b = area_triangle(7,3)
#sum = area_a + area_b
#print("The sum of both areas is: " + str(sum))
#
#def convert_seconds(seconds):
#    hours = seconds // 3600
#    minutes = (seconds - hours * 3600) // 60
#    remaining_seconds = seconds - hours * 3600 - minutes * 60
#    return hours, minutes, remaining_seconds
# 
#hours, minutes, seconds = convert_seconds(5000)
##print(hours, minutes, seconds)

#def convert_seconds(seconds):
#    hours = seconds // 3600
#    minutes = (seconds - hours * 3600) // 60
#    remaining_seconds = seconds - hours * 3600 - minutes * 60
#    return hours, minutes, remaining_seconds
#
#hours, minutes, seconds = convert_seconds(5000)
#print(hours, minutes, seconds)
#
#
#multiplier = 1
#result = multiplier * 5
#while result <= 50:
#    print(result)
#    multiplier += 1
#    result = multiplier * 5
#print("Done")

#for n in range(1, 5, 6):  
#    print(n)
#
#
#for n in range(0,11,2):
#    print(n)
#
## The loop should print 0, 2, 4, 6, 8, 10
#
#for left in range(7):
#  for right in range(left, 7):
#    print("[" + str(left) + "|" + str(right) + "]", end=" ")
#  print()
#
#teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
#for home_team in teams:
#  for away_team in teams:
#    if home_team != away_team:
#      print(home_team + " vs " + away_team)

#
#for n in range(6,18+1,3):
#  print(n*2)
#for n in range(10):
#  print(n+n)

#input = "Four score and seven years ago"
#for c in input:
#  if c.lower() in ['a', 'e', 'i', 'o', 'u']:
##    print(c)
##
##print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])  
#
#for n in range(10):
#  print(n+n)
#
#  def is_power_of(number, base):
# # Base case: when number is smaller than base.
#    if number < base:
#        # If number is equal to 1, it's a power (base**0).
#        return number == 1
#
#    # Recursive case: keep dividing number by base.
#    return is_power_of(number/base, base)
#
#
#print(is_power_of(8,2))     # Should be True
#print(is_power_of(64,4))    # Should be True
#print(is_power_of(70,10))   # Should be False

#Recursion is a process where a function calls itself one or more times with modified values to accomplish a task. 
#This technique can be particularly effective when solving complex problems that can be broken down into smaller, 
#simpler problems of the same type. In the provided code, 
#the count_users function uses recursion to count the number of users that belong to a group within a company's system. It does this by iterating through each member of a group, and if a member is another group, it recursively calls count_users to count the users within that subgroup. However, there is a bug in the code! Can you spot the problem and fix it?


#def count_users(group):
#  count = 0
#  for member in get_members(group):
#    count += 1
#    if is_group(member):
#      count += count_users(member)
#  return count
#
#
#print(count_users("sales")) # Should be 3
#print(count_users("engineering")) # Should be 8
#print(count_users("everyone")) # Should be 18

#In the while loops practice quiz, you were asked to write a function to calculate the sum of all positive numbers between 1 and n. 
# Rewrite the function using recursion instead of a while loop. Remember that when n is less than 1, the function should return 0 as the answer.



#def sum_positive_numbers(n):
#    if n < 1:
#        return 0 
#    return n + sum_positive_numbers(n - 1)
#
#
#print(sum_positive_numbers(3)) # Should be 6
#print(sum_positive_numbers(5)) # Should be 15
#################################################Module 3 Graded Assessment#################################################



#number = 1 # Initialize the variable
#while number < 7: # Complete the while loop condition
#    print(number, end=" ")
#    number + 1 # Increment the variable

#def rows_asterisks(rows):
#    # Complete the outer loop range to control the number of rows
#    for x in range(1,rows+1): 
#        # Complete the inner loop range to control the number of 
#        # asterisks per row
#        for y in range(x): 
#            # Prints one asterisk and one space
#            print("*", end=" ")
#        # An empty print() function inserts a line break at the 
#        # end of the row 
#        print()
#
#
#rows_asterisks(5)
# Should print the asterisk rows shown above


#Fill in the blanks to complete the “counter” function. This function should count down from the “start” to “stop” variables when “start” is bigger than “stop”. 
#Otherwise, it should count up from “start” to “stop”. 
#Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.
#def counter(start, stop):
#    if start > stop:
#        return_string = "Counting down: "
#        while start>=stop: # Complete the while loop
#            return_string+=str(start) # Add the numbers to the "return_string"
#            if start > stop:
#                return_string += ","
#            start-=1 # Increment the appropriate variable
#    else:
#        return_string = "Counting up: "
#        while start<=stop: # Complete the while loop
#            return_string+=str(start) # Add the numbers to the "return_string"
#            if start < stop:
#                return_string += ","
#            start+=1 # Increment the appropriate variable
#    return return_string
#
#
#
#print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
#print(counter(2, 1)) # Should be "Counting down: 2,1"
#print(counter(5, 5)) # Should be "Counting up: 5

#Fill in the blanks to complete the “all_numbers” function. 
#This function should return a space-separated string of all numbers, 
#from the starting   “minimum” variable  up to and including the “maximum” variable that's passed into the function. 
#Complete the for loop so that a function call like “all_numbers(3,6)” will return the numbers “3 4 5 6”.  

##def all_numbers(minimum, maximum):
##
##    return_string = "" # Initializes variable as a string
##
##    # Complete the for loop with a range that includes all 
##    # numbers up to and including the "maximum" value.
##    for n in range(minimum,maximum+1):
##
##        # Complete the body of the loop by appending the number
##        # followed by a space to the "return_string" variable.
##        return_string += str(n) 
##
##    # This .strip command will remove the final " " space 
##    # at the end of the "return_string".
##    return return_string.strip()
##
##
##print(all_numbers(2,6))  # Should be 2 3 4 5 6
##print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
##print(all_numbers(-1,1)) # Should be -1 0 1
##print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
##print(all_numbers(0,0))  # Should be 0


#num1 = 0
#num2 = 0
#
#for x in range(5):
#    num1 = x
#    for y in range(14):
#        num2 = y + 3
#
#print(num1 + num2) # 20