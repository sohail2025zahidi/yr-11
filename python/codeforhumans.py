'''Program that lets the user know if they hold the prerequisites needed to vote in NZ'''
#New Zealand's voting age requirement
voting_age = 18

#ask for user's name and turn into title
name = str(input('What is your name?\n')).title()

#make sure user puts a name when asked
while name == "":
    
    
    name = str(input('What is your name?\n')).title()


#loop to keep asking for an input if not valid
while True:
    
    #try to ask for an age, if the user doesn't comply then try again.
    try:
        
        ask_for_age_int = int(input('How old are you?\n'))
        
        if ask_for_age_int <= -1:
            print('Please enter a valid age')
        
        elif ask_for_age_int < voting_age:
            print('You are too young to vote!')
            break
        
        else:
            break
    
    except ValueError:
        print('Please enter a valid integer')

#If user is old enough, ask if they have residence.
if ask_for_age_int >= voting_age:
    
    while True:
        residency = input('Do you have residence in the country? (yes/no)\n').lower().strip()
        
        if residency == 'yes':
            print(f'Congratulations {name} you can vote in New Zealand!')
            break
        
        elif residency == 'no':
            print('You need residency to vote!')
            break
        
        else:
            print('Please enter yes/no')



