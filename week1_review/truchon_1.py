#hello this is a comment!
#Your Name, Lab #, & Date
#Variable Dictionary 
#total          the sum total of all grades
#people         the num of people in the list 

#-------------------------------------------------

#---IMPORTS---------------------------------------

#---FUNCTIONS-------------------------------------
'''Part 1:
Build a function that is passed both the number of people attending the meeting, as well as the
maximum room capacity. This function should determine the number of people over/under the
capacity based on these two values, and return the difference value.
FUNCTION HEADER: def difference(people, max_cap):
NOTE: when this returned value is positive number, this indicates there are still seats available;
when this returned value is a negative number, this indicates there are people who need to be
removed from the meeting'''
def difference(people, max_cap):
    diff = max_cap - people

    return diff

#test for function
print(f"People: 30, Room Cap: 50, Diff: {difference(30, 50)}")
print(f"People: 33, Room Cap: 25, Diff: {difference(33, 25)}")
print(f"People: 200, Room Cap: 200, Diff: {difference(200, 200)}")

#---MAIN CODE-------------------------------------

ans = "y"
while ans == "y":

    #ensuring user provides numeric values
    try: 
        people = float(input("Enter number of people: "))
        print(f"You entered {people} people")

        try: 
            roomCap = float(input("Enter the room cap: "))
            #continue code you would write if numbers are given
        except:
            print(f"The room cap value MUST be a number")
      

    except:
        print(f"The people value MUST be a number")

    diff = difference(people)
    ans = input("Check another room? [y/n]: ")