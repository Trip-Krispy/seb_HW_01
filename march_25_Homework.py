#March 25 homework

#ask user their first name
print("What's your firs name?")

#prompt user to enter name, store in variable called 'first_Name'
first_Name = input()

#ask user their last name
print("What's your last name?")

#prompt user to enter name, store in variable called 'last_Name'
last_Name = input()

#tell user their full name
print('Nice to meet you ' + first_Name + " " + last_Name)

#ask user age
print('Okay... so how old are you?')

#prompt user to enter age, store in variable called 'age'
age = int(input())

#calucalte user's age in 15 years, store in variable called 'age_15'
age_15 = int(age) + 15

#tell user what their age will be in 15 years
print("According to my calculations, you're going to be " + str(age_15) + " in 15 years! so basically... old")
