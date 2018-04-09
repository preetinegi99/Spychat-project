from spydetails import spy, Spy, Chats  # importing class from spydetails.py
from steganography.steganography import Steganography  # importing Steganography library
from datetime import datetime  # importing datetime library
import csv  # importing csv
from colorama import Fore  # importing Fore from colorama for color
friends = []  # List to load friends
messages = []  # List to load chats
old_status = ["I spy",
              "Watching Titanic",
              "My phone is spying on me",
              "Spy plots are hard,really hard"]  # List of old status


def load_frnds():  # Function to load friends
    with open("friends.csv", "rb") as friend_data:  # Opening file friends.csv
        reader = list(csv.reader(friend_data))  # reading from file
        for row in reader[1:]:
            frnd = Spy(name=row[0], salutation=row[1], age=row[2], rating=row[3])
            friends.append(frnd)  # Appending in the friends list


def load_chats():  # function to load chats
    with open("chats.csv", "rb") as chats:  # opening file chats.csv
        reader = list(csv.reader(chats))  # reading from file
        for row in reader[1:]:  # traversal in the file content
            chat = Chats(time=row[0], sender=row[1], message=row[2], receiver=row[3])
            messages.append(chat)  # Appending the chats in  the list messages

load_frnds()  # loading Friends  automatically by calling load_frnds()
load_chats()  # loading chats automatically by calling load_chats()


def login():  # Function to login
    username = raw_input("Enter your username: ")  # taking username as input
    password = raw_input("Enter your password: ")  # taking password as input
    with open ("login.csv","rb") as login:  # opening login.csv file
        reader = csv.reader(login)  # Reading from file
        for row in reader:
            row = list(reader)  # typecasting to list
            c = 0  # counter
            for i in range(0, len(row)):  # travelling the list
                name = row[i][0]
                pswd = row[i][1]
                sal = row[i][2]
                age = row[i][3]
                rating = row[i][4]
                if name == username:  # checking for correct username
                    if password == pswd:  # checking for correct password
                        spyname = sal+" "+name
                        print 'Welcome !! ' + spyname + ". Your age is " + str(age) + ' and your rating is ' + str(rating)
                        spy_chat(spyname, age, rating)  # calling spy_chats
                        break
                    else:
                        c = 1  # if username is incorrect c=1
                else:
                    c = 2  # if password is incorrect c=2
                i = i+1
        # checking for counter's value
        if c == 1:
            print "Invalid username"
        elif c == 2:
            print "Invalid password"


def show_frnds():  # function to show list of friends
    serial_no = 1  # counter to print serial numbers
    for frnd in friends:  # printing list of friends
        print str(serial_no)+". "+frnd.name
        serial_no = serial_no+1


def select_frnd():  # function to select friend
    show_frnds()  # calling show_frnds()
    print"Select your friend"
    user_selected_frnd = input("Enter your choice: ")  # user selecting friend
    user_selected_frnd_index = user_selected_frnd-1
    return user_selected_frnd_index  # to return the selected friend index


def send_message(spy):  # function for sending message
    selected_friend = select_frnd()  # calling the select_friend function
    receiver = friends[selected_friend].name
    original_image = raw_input("What is the name of original image : ")  # take name of original image as input
    secret_text = raw_input("Enter your secret message : ")  # entering the secret message
    output_path = "output.jpg"  # name of image after encoding the message
    Steganography.encode(original_image, output_path, secret_text)  # calling encode() function to encode message in image
    print "Message Encoded"
    special_msg = ["SOS", "HELP ME", "SAVE ME", "EMERGENCY", "HELP", "SAVE"]  # list of special messages
    message = secret_text.upper()
    sp = message.split(" ")  # spliting the message
    for word in sp:  # checking for special messages in our secret_text
        for i in special_msg:
            if word.upper() == i:
                print Fore.RED + "You have send  an emergence message \n"  # Printing message in red color
                print Fore.BLACK
    time = datetime.now()  # storing the current time
    with open('chats.csv', 'ab') as chats:  # opening file to append chats
        writer = csv.writer(chats)
        writer .writerow([time, spy, secret_text, receiver])  # writing chats to file
    print "Your secret message is ready"


def read_message():  # function for reading message
    selected_friend = select_frnd()  # calling select_friend function
    output_path = raw_input("Which image you want to decode? ")  # the name of image to be decoded
    secret_text = Steganography.decode(output_path)  # calling decode()function to decode
    print "The decoded message is " + secret_text  # printing the secret text


def chat_history():  # function to print chat history
    selected_friend = select_frnd()  # calling select friend
    choice = friends[selected_friend].name
    for i in messages:  # checking for receiver's chats in the list
                if choice == i.receiver:
                    print Fore.BLUE + "Time: " + i.time  # printing time in blue color
                    print Fore.RED + "Receiver: " + i.receiver  # printing receiver in red color
                    print Fore.BLACK + "Message: " + i.msg  # printing message in black color
                

def add_friend():  # function to add friend
    # taking friends detail as input
    frnd = Spy("", "", 0, 0.0)  # class for details of friend
    frnd.name = raw_input("What is your friend's name : ")
    frnd.sal = raw_input("What is your fiends salutation : ")
    frnd.age = input("What is the age :")
    frnd.rating = input("What are the ratings : ")
    frnd.is_online = True
    if len(frnd.name) > 0 and 12 < frnd.age < 50 and frnd.rating > spy.rating:  # checking for spy details
        # writing friends details in file
        with open('friends.csv', 'ab') as friend_data:
            writer = csv.writer(friend_data)
            writer.writerow([frnd.name, frnd.sal, frnd.age, frnd.rating, frnd.is_online])
            print "Your friend is added"
            friends.append(frnd)  # Appending friend in friends list
    else:
        print "The friend cannot be added "
    return len(friends)  # returning length of friends list


def add_status(c_status):  # function to add status
    if c_status is not None:  # checking if the status is none
        print "Your current status is : "+c_status  # printing the current status
    else:
        print "You don't have any status currently"
    existing_status = raw_input("You want to add from old status Y/N? ")  # taking new status from user
    if existing_status.upper() == 'N':
        new_status = raw_input("Enter your status : ")  # taking new status as input
        if len(new_status) > 0:
            updated_status = new_status
            old_status.append(updated_status)  # adding the new status in the status list
        else:
            print "Enter a valid status"
    elif existing_status.upper() == "Y":  # checking if user want to add an old status
        serial_no = 1
        for status in old_status:  # printing the old status
            print str(serial_no)+". "+status
            serial_no = serial_no+1
        status_choice = input("Enter your choice : ")
        updated_status = old_status[status_choice-1]  # updating the status
    return updated_status  # returning the new updated status


def spy_chat(name, age, rating):  # function spy_chat to display menu
    current_status = None
    choice = -1  # choice variable set to -1
    print 'Here are your options ' + name
    while choice != 0:  # while loop will run until user choose to exit
        print '     MENU     \n ' \
              '1.Add a status \n ' \
              '2.Add a friend \n ' \
              '3.Show friends \n'\
              ' 4.Send a message \n '\
              '5.Read  a message\n '\
              '6.Chat history of a friend \n '\
              '7.Logout \n'\
              ' 0.Exit'  # printing menu
        choice = input("Enter your choice:")  # taking choice input
        if choice == 1:  # choice 1
            current_status = add_status(current_status)
            print "Updated status is : "+current_status
        elif choice == 2:  # choice 2
            friend_no = 1  # counter to print no. of friends
            no_of_friends = add_friend()  # calling function add_friend to add friend
            print " You have "+str(no_of_friends)+" number of friends"  # printing number of friends
        elif choice == 3:
            show_frnds()
        elif choice == 4:
            send_message(name)  # calling send_message()function
        elif choice == 5:
            read_message()  # calling the read_message()function
        elif choice == 6:  # to read a user's message
            print chat_history()  # calling chat_history function
        elif choice == 7:  # logout option
            reply = raw_input("Are you sure you want to logout Y/N?? ")
            if reply.upper() == "Y":
                print Fore.MAGENTA + "You are logged out....\n"  # printing message of logout in magenta color
                print Fore.BLACK
                print"<------------EXIT-------------->"
                break
        elif choice == 0:  # exit
            print 'Exit'
        else:  # for any invalid input
                print 'Invalid input'


def signup():
    spy = Spy("", "", 0, 0.0)  # class for spydetails
    spy.name = raw_input('Enter your username: ')  # take name as input from user
    if spy.name.isspace():  # to check for space input
        print 'Enter a valid name '
    elif spy.name.isdigit():  # to check for digit input
        print 'Enter a valid name '
    elif len(spy.name) > 2:  # checking for length of the string name
        password=raw_input("Enter your password: ")
        print 'Welcome ' + spy.name + ' ' + 'glad to have you back with us.'  # concatenating strings
        spy.sal = raw_input('What should we call you (Mr.or Ms.): ')
        if spy.sal.upper() == 'MR.' or spy.sal.upper() == 'MS.':  # using if
            spy_name = spy.sal + " " + spy.name
            print 'Alright ' + spy_name + '. I\'d like to know a little bit more about you...'
            spy.age = input('What\'s your age :  ')
            if 50 <= spy.age <= 12:  # nested if statement to check range of age
                print 'You are not eligible to be a spy.'
            else:
                spy.rating = input('What are your ratings : ')  # taking ratings as input
                if spy.rating > 5:
                    print 'Great Spy!!'
                elif spy.rating > 3.5:  # elif statement for more than one condition
                    print 'Average Spy.'
                elif spy.rating > 2.5:
                    print 'Need to work hard!!'
                else:
                    print 'Who hired you'
                spy_is_online = True
                print 'Authentication complete. Welcome ' + spy_name + '.Your age is ' + str(spy.age) + ' and your rating is ' + str(spy.rating)  # typecasting of integer to string
                # writing details in login file
                with open("login.csv", "ab")as login:
                    writer = csv.writer(login)
                    writer.writerow([spy.name, password, spy.sal, spy.age, spy.rating, spy_is_online])

                spy_chat(spy_name, spy.age, spy.rating)  # calling function spy_chat

        else:
            print 'Enter a valid salutation'

    else:
        print 'Ooops! Enter a valid name '


def welcome():
        f = datetime.now()  # calling function now() from datetime library
        print f.strftime("%b %d %Y %H:%M:%S")  # use of string time format
        print 'Hello...!! Welcome to SPYCHAT.'  # printing hello
        print 'Let\'s get started'
        spy_reply = raw_input('Are you a new user? Y/N ')  # asking the user if he is a new user or not
        if spy_reply.upper() == 'N':
            login()
        elif spy_reply.upper() == 'Y':
                signup()
        else:
            print "Invalid input"
welcome()



