#SE 126
# Lab #1C
#
# Variables used:
# max_room      maximum number of occupants allowed in the room
# attending     the number of people registering for the event
# over_under    represents the number of people who cannot attend the event or
#               the number of people who still can register for the event
# more_rooms    prompt used to aske if the user has any more rooms to enter
#
# Functions:
# capacity      prompts the user for the maximum number of people the room can hold and returns that value
#               Variable: returns max which is the maximum number of occupants allowed in the room
#                
# attendees     prompt ths user for the number of people who want to register for that room and returns
#               the value.  Variable: returns people which represents the number of people who want to
#                register
#
# register      requires that two parameters maximum numbeer of people the room can hold and the number of 
#               people who want to register.  It returns a value that represents how many more people can 
#               register or how many people have to be told they cannot attend the event.
#               Variables: returns amount which is the amount of people who can attend or number of people
#               that have to be told they cannot attend.
#
# more_data     prompts the user to see if they want to check more rooms.  Returns a character (y/n)
#               Variable: returns data which is either a y or n

#Functions
# =============================================================================================

def capacity():
    max = int(input("What is the capacity of the room? "))
    return max

def attendees():
    number = int(input("How many people want to attend the event? "))
    return number

def register(max, number):
    amount = max - number
    return amount

def more_data():
    data = input("Do you want to check anymore rooms (y/n)? ")
    data = data.lower()
    while(data!= "y" and data != "n"):
        data = input("Do you want to check anymore rooms (y/n)? ")
        data = data.lower()

    return data


more_rooms = "y"
while(more_rooms == "y"):
    max_room = capacity()
    attending = attendees()
    
    over_under = register(max_room, attending)
   
    if(over_under >= 0):
        print("The conference can be held.", over_under, " more people can attend.")
    else:
        print(abs(over_under), "people have to be told they cannot attend the meeting.")
   
    more_rooms = more_data()
   

print()
print()
print("Processing has been completed!!!")

