import csv 
records = 0
with open("week2_practice/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        machine = rec[0]
        if rec[0] == "D":
            machine = "Desktop"
        else:
            machine = "Laptop"

        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        numdisk = int(rec[5])

        if numdisk == 1:
            #only 1 hdd
            disk2 = "n/a"
            os = rec[6]
            year =  ___    