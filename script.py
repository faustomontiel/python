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

#number = 1 # Initialize the variable
#while number < 7: # Complete the while loop condition
#    print(number, end=" ")
#    number + 1 # Increment the variable

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(1,rows+1): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above
