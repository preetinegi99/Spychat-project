print 'Hello!'
name=raw_input('Enter your name ' )#take name as input from user
if len(name)>2:#checking for length of the string name
    print 'Welcome '+name+' '+'glad to have you back with us.'#concatenating strings
    salutation=raw_input('What should we call you (Mr.or Ms.) ' )
    if salutation=='Mr.'or salutation=='Ms.':#using if to check condition to take input of salutaion
        spy_name=salutation+" "+name
        print 'Alright '+spy_name+'. I\'d like to know a little bit more about you...'
        age=input('What\'s your age ')
        if 50<=age<=12:#nested if statement to check range of age
            print 'You are not eligible to be a spy'
        else:
            rating=input('What are your ratings ')
            if rating>5:
                print 'Great Spy!!'
            elif rating >3.5:#elif statement for more than one condition
                print 'Average Spy'
            elif rating>2.5:
                print 'Need to work hard!!'
            else:
                print 'Who hired you'
            spy_is_online = True
            print 'Authentication complete. Welcome ' + spy_name + ' age: ' + str(age) + ' ratings: ' + str(rating)#typecasting of integer to string

    else:
        print 'Enter a vaild salutation'
elif name.isspace():#to check for space
    print 'Please enter a valid name.'

else:
    print 'Ooops! Enter a valid name '


