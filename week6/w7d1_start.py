
#1D PARALLEL LISTS FOR SEATS--------------------------------------------------------
#create lists for map - each list reps a SEAT "column"
seatA = []
seatB = []
seatC = []
seatD = []

#there are 4 rows, populate a seat for each list and each row
for i in range(0, 4):
    seatA.append("X")
    seatB.append("X")
    seatC.append("X")
    seatD.append("X")

#display the map
print(f"[{"ROW":3}]\t{" A ":3}   {" B ":3}  |  |  {" C ":3}   {" D ":3}")
print("-----------------------------------------------------------------")
for i in range(0, len(seatA)):
    print(f"[{i+1:3}]\t{seatA[i]:3}   {seatB[i]:3}  |  |  {seatC[i]:3}   {seatD[i]:3}")



#2D ENTIRE MAP FOR ALL SEATS--------------------------------------------------------

#create the map list
seatMap = []

#15 rows of 30 seats for theater
for i in range(0, 15):
    tempRow = []
    for x in range(0, 30):
        tempRow.append("X")
    seatMap.append(tempRow)

#display the seat map 
print(f"[ROW]  A B C D E F G H |  | I J K L M N O P Q R S T U V W X Y Z 1 2 3 4")
for i in range(0, len(seatMap)):
    #map has 15 rows; for each row we need to print the entire list of seats! 
    print(f"[{i+1:3}] ", end=" ")
    for x in range(0, len(seatMap[i])):
        if x == 8:
            print(f"|  | {seatMap[i][x]}", end=" ")
        else:
            print(f"{seatMap[i][x]}", end=" ")
    print() #bumps next row of seats to next line/row in map