#WEEK 3 DAY 1: LIST DEMO

#LISTS can hold multiple points of data and store them to "memory" to be used later on in our program

#this demo utilizes the lab 2B solution file


#VARIABLE DICTIONARY----------------------------
#records            total records in file

#field0             col. 0, rec[0], type of machine, from file
#device               a LIST that holds the entire field0/rec[0] data from file
 
#field1             col. 1, rec[1], brand of machine, from file
#brand              a LIST that holds the entire field1/rec[1] data from file

#field2             col. 2, rec[2], cpu, from file
#cpu                a LIST that holds the entire field2/rec[2] data from file

#field3             col. 3, rec[3], ram, from file
#ram                a LIST that holds the entire field3/rec[3] data from file

#field4             col. 4, rec[4], 1st disk space, from file
#first_disk         a LIST that holds the entire field4/rec[4] data from file


#field5*             col. 5, rec[5], number of hard drives*, from file
#                           *this value determines where the remaining record values are stored
#num_disks          a LIST that holds the entire field5/rec[5] data from file

#field6             col. 6, 2nd disk space, from file where rec[5] == "2"
#secnd_disk         a LIST that holds the entire field6/rec[6] data from file

#field7             col. 7, operating system, from file 
#os                 a LIST that holds the entire field7/rec[7] data from file

#field8             col. 8, year, from file 
#yr                 a LIST that holds the entire field8/rec[8] data from file



#*this value determines where the remaining record values are stored

#BASE PROGRAM CODE-----------------------------------------------------------------------------------------

import csv 

#initialize variable that will count the total number of records -- NECESSARY FOR LIST PROCESSING LATER
records = 0

#create some empty lists - one list for every possible field in the file
device = []
brand = []
cpu = []
ram =[]
first_disk = []
second_disk = []
num_disks = []
os = []
yr = []

with open("week3/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #update the records value
        records += 1

        #adding data to lists -> .append()
        #device.append(rec[0])
        if rec[0] == "D":
            device.append("Desktop")
        elif rec[0] == "L":
            device.append("Laptop")
        else:
            device.append("-DEV ERROR-")

        if rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        elif rec[1] == "DL":
            brand.append("Dell")
        else:
            brand.append("-BRAND ERROR-")

        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_disks.append(int(rec[5]))

        if int(rec[5]) == 1:
            second_disk.append("---")
            os.append(rec[6])
            yr.append(rec[7])
        elif int(rec[5]) == 2:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
        else:
            second_disk.append("-ERROR ")
            os.append(" @ ")
            yr.append(f"rec# {records}-")

#process the list(s) to view their storage
for index in range(0, records):
    #"for every index starting at 0 and up to the number of records"
    print(f"{device[index]:10}\t{brand[index]:10}\t...") #this line prints for every index found within the device list

#len() --> length function; returns integer, num of items in list it is passed
desktops = 0
for i in range(0, len(device)):

    if device[i] == "Desktop":
        desktops += 1

print(f"There are {desktops} desktops in this file.")

laptops = 0
for value in device:
    if value == "Laptop":
        laptops += 1
print(f"There are {laptops} laptops in this file.")      