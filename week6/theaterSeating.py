#----IMPORTS-------------------------------------------------

#----FUNCTIONS-----------------------------------------------
def display():
    #display seatMap 
    print("     A B C D E F G H    I J K L M N O P Q R S T U V    W X Y Z 1 2 3 4") #row letter label
    for i in range(0, len(seatMap)):
        print(f"{i + 1:3}: ", end = "") #row number label
        for x in range(0, len(seatMap[i])):
            if x != 8 and x != 22:
                print(f"{seatMap[i][x]}", end=" ")
            else:
                print(f"| |{seatMap[i][x]}", end=" ")    
        print()
#----MAIN CODE-----------------------------------------------

#create the theater seat lists - 2D list, length of 15 on each interior
seatMap = []
rowList = []

seats = "ABCDEFGHIJLMNOPQRSTUVWXYZ1234"

for x in range(0, 15):
    #x --> row num, j --> indiv seat
    for j in range(0, 30):
        rowList.append("#") #adds seats to rows
    seatMap.append(rowList) #adds full row to map
    rowList = []  #clears seats in row for next row

display()