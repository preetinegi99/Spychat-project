from spydetails import spy_rating,spy_age,spy_name #importing variables from spydetails.py
def spy_chat(spy_name,spy_age,spy_rating): #function spy_chat to display menu
    choice= -1 #choice variable set to -1
    print 'Here are your options ' + spy_name
    while choice!=0: #while loop will run until user choose to exit
        print '     MENU     \n 1.Add a status \n 2.Add a friend \n 0.Exit' #printing menu
        choice=input("Enter your choice:") #taking choice input
        if choice==1: #choice 1
            print 'will add a status'
        elif choice==2: #choice 2
            print 'will add a friend'
        elif choice==0: #exit
            print 'Exit'
        else:  #for any invalid input
                print 'Invalid input'

print 'Hello...!!' #printing hello
print 'Let\'s get started'
spy_reply=raw_input('Are you a new user? Y/N ') #asking the user if he is a new user or not
if spy_reply.upper()=='N':
    print 'Welcome back!! '+spy_name+' . Your age is '+str(spy_age)+' and your rating is '+ str(spy_rating)
    spy_chat(spy_name,spy_age,spy_rating) #calling function spy_chat
elif spy_reply.upper()=='Y':
    name=raw_input('Enter your name ') #take name as input from user
    if name.isspace(): #to check for space input
        print 'Enter a valid name'
    elif name.isdigit(): #to check for digit input
        print 'Enter a valid name'
    elif len(name)>2: #checking for length of the string name
        print 'Welcome '+name+' '+'glad to have you back with us.' #concatenating strings
        salutation=raw_input('What should we call you (Mr.or Ms.) ' )
        if salutation=='Mr.'or salutation=='Ms.': #using if
            spy_name=salutation+" "+name
            print 'Alright '+spy_name+'. I\'d like to know a little bit more about you...'
            age=input('What\'s your age ')
            if 50<=age<=12: #nested if statement to check range of age
                print 'You are not eligible to be a spy'
            else:
                rating=input('What are your ratings ')
                if rating>5:
                    print 'Great Spy!!'
                elif rating >3.5: #elif statement for more than one condition
                    print 'Average Spy'
                elif rating>2.5:
                    print 'Need to work hard!!'
                else:
                    print 'Who hired you'
                spy_is_online = True
                print 'Authentication complete. Welcome ' + spy_name + '.Your age is ' + str(age) + ' and your rating is ' + str(rating)#typecasting of integer to string
                spy_chat(spy_name,spy_age,spy_rating) #calling function spy_chat

        else:
            print 'Enter a vaild salutation'

    else:
        print 'Ooops! Enter a valid name '


