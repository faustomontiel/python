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
#################################################Module 3 Graded Assessment#################################################
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



#################################################Module 4 Strings#################################################

#message = "A kong string with a silly typo"
#new_message = message[0:2] + "l" + message[3:]
#print(new_message)
#
#message = "This is a new message"
#print(message)
#message = "And another one"
#print(message)
#
#pets="Cats & Dogs"
#pets.index("&")
#pets.index("C")
#pets.index("Dog")
#pets.index("s")
#
#
#def replace_domain(email, old_domain, new_domain):
#  if "@" + old_domain in email:
#    index = email.index("@" + old_domain)
#    new_email = email[:index] + "@" + new_domain
#    return new_email
#  return email
#
#
#animals = "lions tigers and bears"
#animals.index("g")
#
#
#animals = "lions tigers and bears"
#animals.index("bears")
#
#
#animals = "lions tigers and bears"
#"horses" in animals
#
#animals = "lions tigers and bears"
#"tigers" in animals
#
#
#"Mountains".upper()
#"Mountains".lower()
#
#answer = "YES"
#if answer.lower() == "yes":
#  print("User said yes")
#
#" yes ".strip()
#" yes ".lstrip()
#" yes ".rstrip()
#
#"The number of times e occurs in this string is 4".count("e")
#
#"Forest".endswith("rest")
#
#"Forest".isnumeric()
#"12345".isnumeric()
#
#int("12345") + int("54321")
#
#" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
#"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
#
#"This is another example".split()

#fortmatting

#name = "Manny"
#number = len(name) * 3
#print("Hello {}, your lucky number is {}".format(name, number))
#Hello Manny, your lucky number is 15
#
#
#name = "Manny"
#print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
#Your lucky number is 15, Manny.
#
#price = 7.5
#with_tax = price * 1.09
#print(price, with_tax)
#print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
#7.5 8.175
#Base price: $7.50. With Tax: $8.18
#
#
#def to_celsius(x):
#  return (x-32)*5/9
#
#for x in range(0,101,10):
#  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
# 0 F | -17.78 C
# 10 F | -12.22 C
# 20 F |  -6.67 C
# 30 F |  -1.11 C
# 40 F |   4.44 C
# 50 F |  10.00 C
# 60 F |  15.56 C
# 70 F |  21.11 C
# 80 F |  26.67 C
# 90 F |  32.22 C
#100 F |  37.78 C


# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
#basket = [
#    ("Peaches", 3.0, 2.99),
#    ("Pears", 5.0, 1.66),
#    ("Plums", 2.5, 3.99)
#]
#
#
## Calculate the total price for each item (weight times price per pound)
## and add them up to get a subtotal.
##
#subtotal = 0.00
#for item in basket:
#  fruit, weight, unit_price = item
#  subtotal += (weight * unit_price)
#
#
## Now calculate the sales tax and total bill.
##
#tax_rate = 0.06625  # 6.625% sales tax in New Jersey
#tax_amt = subtotal * tax_rate
#total = subtotal + tax_amt
#
#
## Print the receipt for the customer.
##
#print("Subtotal:", subtotal)
#print("Sales Tax:", tax_amt)
#print("Total:", total)

#def is_palindrome(input_string):
#    # Two variables are initialized as string date types using empty 
#    # quotes: "reverse_string" to hold the "input_string" in reverse
#    # order and "new_string" to hold the "input_string" minus the 
#    # spaces between words, if any are found.
#    new_string = ""
#    reverse_string = ""
#
#    # Complete the for loop to iterate through each letter of the
#    # "input_string"
#    for letter in input_string:
#
#        # The if-statement checks if the "letter" is not a space.
#        if letter != " ":
#
#            # If True, add the "letter" to the end of "new_string" and
#            # to the front of "reverse_string". If False (if a space
#            # is detected), no action is needed. Exit the if-block.
#            new_string = new_string + letter
#            reverse_string = letter + reverse_string
#
#    # Complete the if-statement to compare the "new_string" to the
#    # "reverse_string". Remember that Python is case-sensitive when
#    # creating the string comparison code. 
#    if new_string.lower() == reverse_string.lower():
#
#        # If True, the "input_string" contains a palindrome.
#        return True
#		
#    # Otherwise, return False.
#    return False
#
#
#print(is_palindrome("Never Odd or Even")) # Should be True
#print(is_palindrome("abc")) # Should be False
#print(is_palindrome("kayak")) # Should be True
#
#
#
#
#def convert_distance(miles):
#    km = miles * 1.6 
#    result = "{} miles equals {:.1f} km".format(miles,km)
#    return result
#
#
#print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
#print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
#print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
#
#
#def nametag(first_name, last_name):
#    return("{firstName} {lastNameLetter}."
#    .format(firstName=first_name,lastNameLetter=last_name[0].upper()))
#
#
#print(nametag("Jane", "Smith")) 
## Should display "Jane S." 
#print(nametag("Francesco", "Rinaldi")) 
## Should display "Francesco R." 
#print(nametag("Jean-Luc", "Grand-Pierre")) 
## Should display "Jean-Luc G." 



#def replace_ending(sentence, old, new):
#    # Check if the old substring is at the end of the sentence 
#    if sentence.endswith(old):
#        # Using i as the slicing index, combine the part
#        # of the sentence up to the matched string at the 
#        # end with the new string
#        i = len(sentence) - len(old)
#        new_sentence = sentence[:i] + new
#        return new_sentence
#
#
#    # Return the original sentence if there is no match 
#    return sentence
#    
#print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
## Should display "It's raining cats and dogs"
##print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
### Should display "She sells seashells by the seashore"
##print(replace_ending("The weather is nice in May", "may", "april")) 
### Should display "The weather is nice in May"
##print(replace_ending("The weather is nice in May", "May", "April")) 
### Should display "The weather is nice in April"
#
##LIST
#
#x = ["Now", "we", "are", "cooking!"]
#
#x = ["Now", "we", "are", "cooking!"]
#"are" in x
#
#x = ["Now", "we", "are", "cooking!"]
#print(x[0])
#print(x[3])
#
#x = ["Now", "we", "are", "cooking!"]
#x[1:3]
#
#
#fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#fruits.append("Kiwi")
#print(fruits)
#
#fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#fruits.insert(0, "Orange")
#print(fruits)
#
#fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#fruits.insert(0, "Orange")
#fruits.insert(25, "Peach")
#print(fruits)
#
#fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#fruits.insert(0, "Orange")
#fruits.insert(25, "Peach")
#fruits.remove("Melon")
#print(fruits)
#
#
#fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#fruits.insert(0, "Orange")
#fruits.insert(25, "Peach")
#fruits.remove("Melon")
#fruits.pop(3)
#print(fruits)
#
#fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#fruits.insert(0, "Orange")
#fruits.insert(25, "Peach")
#fruits.remove("Melon")
#fruits.pop(3)
#fruits[2] = "Strawberry"
#print(fruits)
#
#
#def convert_seconds(seconds):
#  hours = seconds // 3600
#  minutes = (seconds - hours * 3600) // 60
#  remaining_seconds = seconds - hours * 3600 - minutes * 60
#  return hours, minutes, remaining_seconds
#result = convert_seconds(5000)
#print(result)
#
#def convert_seconds(seconds):
#  hours = seconds // 3600
#  minutes = (seconds - hours * 3600) // 60
#  remaining_seconds = seconds - hours * 3600 - minutes * 60
#  return hours, minutes, remaining_seconds
#result = convert_seconds(5000)
#hours, minutes, seconds = result
#print(hours, minutes, seconds)
#
#def convert_seconds(seconds):
#  hours = seconds // 3600
#  minutes = (seconds - hours * 3600) // 60
#  remaining_seconds = seconds - hours * 3600 - minutes * 60
#  return hours, minutes, remaining_seconds
#hours, minutes, seconds = convert_seconds(1000)
#print(hours, minutes, seconds)
#
#
#
#animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
#chars = 0
#for animal in animals:
#  chars += len(animal)
#
#print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
#
#
#winners = ["Ashley", "Dylan", "Reese"]
#for index, person in enumerate(winners):
#  print("{} - {}".format(index + 1, person))
#
#
#def full_emails(people):
#  result = []
#  for email, name in people:
#    result.append("{} <{}>".format(name, email))
#  return result
#print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
#
#
#multiples = []
#for x in range(1,11):
#  multiples.append(x*7)
#
#print(multiples)
#
#
#multiples = [x*7 for x in range(1,11)]
#print(multiples)
#
#
#languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
#lengths = [len(language) for language in languages]
#print(lengths)
#
#z = [x for x in range(0,101) if x % 3 == 0]
#print(z)
#
#
##List Comprehension Examples
#
#
## Create a list of tuples where each tuple contains the numbers 1, 2, and 3.
#numbers = [(1, 2, 3) for _ in range(5)]
#
#### Simple List Comprehension
#print("List comprehension result:")
#
## The following list comprehension compacts several lines 
## of code into one line:
#print([x*2 for x in range(1,11)])
#
#### Long form for loop
#print("Long form code result:")
#
## The list comprehension above accomplishes the same result as
## the long form version of the code shown below:
#my_list = []
#for x in range(1,11):
#    my_list.append(x*2)
#print(my_list)
#
## Select Run to compare the two results.
#




#
#filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
## Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

#Pregunta 1
#Fill in the blank using a for loop. With the given list of "filenames", this code should rename all files with the extension .hpp to the extension .h. 
#The code  should then generate a new list called "new_filenames" that contains the file names with the new extension.
#
#You are given a list of filenames like this:

#filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


#new_filenames = []
#for filename in filenames:
#    if filename.endswith("hpp"):
#        new_filenames.append(filename.replace("hpp","h"))
#    else:
#        new_filenames.append(filename)
#
#
#print(new_filenames)
## Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
#
#
#filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
## Generar new_filenames como una lista que contiene los nuevos nombres de archivos
#new_filenames = [filename[:-4] + ".h" if filename.endswith(".hpp") else filename for filename in filenames]
#print(new_filenames)
## Debería mostrar ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
#
#
#print(new_filenames) 
## Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
#
##Create a function that turns text into pig latin. Pig latin is a simple text transformation that modifies each word by:
##moving the first character to the end of each word;
##then appending the letters "ay" to the end of each word.
##For example, python ends up as ythonpay.
#
#def pig_latin(text):
#  say = ""
#  # Separate the text into words
#  words = words = text.split()
#  for word in words:
#    # Create the pig latin word and add it to the list
#    say += word[1:]+word[0]+ "ay " 
#    # Turn the list back into a phrase
#  return say
#    
#print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
#print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
#
#
##Fill in the blanks to complete the “biography_list” function. The “biography_list” function reads in a list of tuples “people”, 
## which contains the name, age, and profession of each “person”. Then, prints the sentence "__ is _ years old and works as __.". 
## For example, “biography_list([("Ira", 30, "a Chef")])” should print: “Ira is 30 years old and works as a Chef.” 
#
#def biography_list(people):
#    # Iterate over each "person" in the given "people" list of tuples. 
#    for person in people:
#
#
#        # Separate the 3 items in each tuple into 3 variables:
#        # "name", "age", and "profession"   
#        name, age, profession = person  
#        # Format the required sentence and place the 3 variables 
#        # in the correct placeholders using the .format() method.
#        print("{} is {} years old and works as {}".format(name,age,profession))
#
#
## Call to the function:
#biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])
#
#
## Click Run to submit code
#
#
## Output should match:
## Ira is 30 years old and works as a Chef
## Raj is 35 years old and works as a Lawyer
## Maria is 25 years old and works as an Engineer

##DICTIONARY

#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#print(file_counts)
#
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#file_counts["txt"]
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#"jpg" in file_counts
#"html" in file_counts
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#file_counts["cfg"] = 8
#print(file_counts)
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#file_counts["csv"] = 17
#print(file_counts)
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23, 'cfg':8}
#del file_counts["cfg"]
#print(file_counts)
#
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#for extension in file_counts:
#  print(extension)
#
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#for ext, amount in file_counts.items():
#  print("There are {} files with the .{} extension".format(amount, ext))
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#file_counts.keys()
#file_counts.values()
#
#file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#for value in file_counts.values():
#  print(value)
#
#def count_letters(text):
#  result = {}
#  for letter in text:
#    if letter not in result:
#      result[letter] = 0
#    result[letter] += 1
#  return result
#count_letters("aaaaa")
#count_letters("tenant")
#count_letters("a long string with a lot of letters") 



#The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).


#def email_list(domains):
#    emails = []
#    for domain, users in domains.items():
#        for user in users:
#            emails.append(user+ "@" +domain)
#    return emails
#
#print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#The groups_per_user function receives a dictionary, which contains group names with the list of users. 
#Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

#
#def groups_per_user(group_dictionary):
#    user_groups = {}
#	# Go through group_dictionary
#    for group, users in group_dictionary.items():
#		# Now go through the users in the group
#        for user in users:
#			# Now add the group to the the list of
#            # groups for this user, creating the entry
#            # in the dictionary if necessary
#            if user not in user_groups:
#             user_groups[user] = []
#            user_groups[user].append(group) 
#    return(user_groups)
#
#print(groups_per_user({"local": ["admin", "userA"],
#		"public":  ["admin", "userB"],
#		"administrator": ["admin"] }))
#
#
#def add_prices(basket):
#	# Initialize the variable that will be used for the calculation
#	total = 0
#	# Iterate through the dictionary items
#	for value in basket.values():
#		# Add each price to the total calculation
#		# Hint: how do you access the values of
#		# dictionary items?
#		total += value
#	# Limit the return value to 2 decimal places
#	return round(total, 2)  
#
#groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
#	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
#
#print(add_prices(groceries)) # Should print 28.44
#wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
#new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
#wardrobe.update(new_items)
#print(wardrobe)

#
#
#class Apple:
#    def __init__(self):
#        self.color = "red"
#        self.flavor = "sweet"
#
#honeycrisp = Apple()
#print(honeycrisp.color)
#
## prints "red"
#
#
##The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.
#
#
#def add_prices(basket):
#	# Initialize the variable that will be used for the calculation
#	total = 0
#	# Iterate through the dictionary items
#	for value in basket.values():
#		# Add each price to the total calculation
#		# Hint: how do you access the values of
#		# dictionary items?
#		total += value
#	# Limit the return value to 2 decimal places
#	return round(total, 2)  
#
#groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
#	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
#
#print(add_prices(groceries)) # Should print 28.44


#The format of the input variable “address_string” is: numeric house number, followed by the street name which may contain numbers and could be several words long (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive"). 

#Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street". This function should:

#accept a string through the parameters of the function;

#separate the address string into new strings: house_number and street_name; 

#return the variables in the string format: "House number X on a street named Y". 


#def format_address(address_string):
#
#    house_number = ""
#    street_name = ""
#    # Separate the house number from the street name.
#    address_parts = address_string.split()
#    
#    for address_part in address_parts:
#       # Complete the if-statement with a string method.  
#       if address_part.isnumeric():
#         house_number = address_part
#       else:
#         street_name += address_part + " "
#    # Remove the extra space at the end of the last "street_name".
#    street_name = street_name.strip()
# 
#    # Use a string method to return the required formatted string.
#    return ("House number {} on a street named {}").format(house_number,street_name)
#
#
#print(format_address("123 Main Street"))
## Should print: "House number 123 on a street named Main Street"
#
#
#print(format_address("1001 1st Ave"))
## Should print: "House number 1001 on a street named 1st Ave"
#
#
#print(format_address("55 North Center Drive"))
## Should print "House number 55 on a street named North Center Drive"
#
#
#def alpha_length(string):
#    character = ""
#    count_alpha = 0
#    # Complete the for loop sequence to iterate over "string".
#    for letter in string: 
#        # Complete the if-statement using a string method. 
#        if letter.isalpha():
#            count_alpha += 1  
#    return count_alpha
# 
#print(alpha_length("This has 1 number in it")) # Should print 17
#print(alpha_length("Thisisallletters")) # Should print 16
#print(alpha_length("This one has punctuation!")) # Should print 21


#def sort_distance(distances):
#    distances.sort() # Sort the list
#    distances.reverse() # Reverse the order of the list
#    return distances
#
#
#print(sort_distance([2,4,0,15,8,9]))
## Should print [15, 9, 8, 4, 2, 0]
#
#def even_numbers(first, last):
#  return [ n for n in range(first,last) if n%2 ==0]
#
#
#print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
#print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
#print(even_numbers(2, 7))  # Should print [2, 4, 6]


#def countries(countries_dict):
#    result = ""
#    # Complete the for loop to iterate through the key and value items 
#    # in the dictionary.
#    for countries in countries_dict.values():
#        # Use a string method to format the required string.
#        result += str(countries) + "\n"
#    return result
#
#print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']


#def setup_guests(guest_list):
#    # loop over the guest list and add each guest to the dictionary with
#    # an initial value of 0
#    result = {} # Initialize a new dictionary 
#    for guest in guest_list: # Iterate over the elements in the list 
#        if guest not in result:
#            result[guest] = [] # Add each list element to the dictionary as a key with
#        result[guest].append(0) # the starting value of 0             
#    return result
#
#guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]
#
#print(setup_guests(guests))
## Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}
#
#
#def count_letters(text):
#  # Initialize a new dictionary.
#  dictionary = {} 
#  # Complete the for loop to iterate through each "text" character and 
#  # use a string method to ensure all letters are lowercase.
#  for letter in text:   
#    # Complete the if-statement using a string method to check if the
#    # character is a letter.
#    if letter.isalpha(): 
#      # Complete the if-statement using a logical operator to check if 
#      # the letter is not already in the dictionary.
#      if letter.lower() not in dictionary:
#           # Use a dictionary operation to add the letter as a key
#           # and set the initial count value to zero.
#           dictionary[letter.lower()] = 0 
#      # Use a dictionary operation to increment the letter count value 
#      # for the existing key.
#      dictionary[letter.lower()] += 1 
#  return dictionary
#
#print(count_letters("AaBbCc"))
## Should be {'a': 2, 'b': 2, 'c': 2}
#
#print(count_letters("Math is fun! 2+2=4"))
## Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
#
#print(count_letters("This is a sentence."))
## Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}



#numbers = [ 4, 6, 2, 7, 1 ]
#numbers.sort()
#print(numbers)
#
#
#names = ["Carlos", "Ray", "Alex", "Kelly"]
#print(sorted(names))
#print(names)
#print(sorted(names, key=len))

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout": 
       if event.user in machines[event.machine] and event.type == "login":
        machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user



events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)