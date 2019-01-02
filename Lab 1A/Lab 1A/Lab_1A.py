#SE 126
# Lab #1A
#
# Variables used:
# max_room      maximum number of occupants allowed in the room
# attending     the number of people registering for the event
# over_under    represents the number of people who cannot attend the event or
#               the number of people who still can register for the event
# more_rooms    prompt used to aske if the user has any more rooms to enter
#
# Notes:
#   Line 23 abs(over_under) --- returns the absolute value of the number over_under
#   Could have used -1 * over_under
#   Line 22 could have changed the if statement to the following
#   if(over_under > 0):
#       print("The conference can be held.", over_under, " more people can attend.")
#    elseif(over_under < 0):
#       print(abs(over_under), "people have to be told they cannot attend.")
#    else:
#       print("The meeting can be held but no more registrations will be accepted.")

more_rooms = "y"
while(more_rooms == "y"):
    max_room = int(input("What is the capacity of the room? "))
    attending = int(input("How many people want to attend the event? "))
    print()

    over_under = max_room - attending
    if(over_under >= 0):
        print("The conference can be held.", over_under, " more people can attend.")
    else:
        print(abs(over_under), "people have to be told they cannot attend the meeting.")

    print()
    print()
    more_rooms = input("Do you want to check anymore rooms (y/n)? ")
    more_rooms = more_rooms.lower()

print()
print()
print("Processing has been completed!!!")

