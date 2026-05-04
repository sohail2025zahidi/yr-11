'''' this is a bit of code to check if the user can vote'''
#ask the user for name
name = input("What is your name ")
print(f"hello {name}")
while True:
  try:
    #ask for user age
    age = int(input(f"How old are you {name}? "))
    break
  except:
    print('That is not a number')
#end of loop

#ask if user is a resident
while True:
  is_resident = input(f"And {name} are you a resident? yes or no. ").lower()
  if is_resident == 'yes':
    is_resident = True
    break
  elif is_resident == 'no':
    is_resident = False
    break
  else:
    print('Please enter corrctly')
#do final check to see if user is able to vote
if age >= 17 and is_resident == True:
  print('You can vote')
else:
  print(f'Sorry {name} you cant vote')
