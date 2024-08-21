#Alex Zayat
#Program Explanation: This program helps the user find vehicles they may be interested in based on user inputs. After showing results, the program allows the user to enter more inputs or exit the program




import csv
record = 0
records = 0
answer = 0
response = 0
#--create lists---------------------------------
modelYear = []
manufacturer = []
model = []
transmission = []
price = []
Mcars = []
#----------disconnect----------------------------


with open("midterms/alex/vehicles.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        # Append each field to the corresponding list
        modelYear.append(rec[0])
        manufacturer.append(rec[1])
        model.append(rec[2])
        transmission.append(rec[3])
        price.append(rec[4])

        # Increment the records counter
        record += 1


print("\tNew Car Finder Assistant")

answer = "y"  # Loop by checking for user input

while answer == "y":
    # Ask the user for transmission type
    answer = input("\nAre you looking for an Automatic or Manual? ").lower()

    # Ask the user for vehicle type
    response = input("Are you looking for a Sedan or SUV? ").lower()

    # Check conditions for Automatic and Sedan
    if answer.lower() == "automatic" and response.lower() == "sedan":
        for index in range(0, 2):

            print(f"{modelYear[index]:<5}\t{manufacturer[index]:<10}\t{model[index]:<10}\t${price[index]:>5}") 


    #Check conditions for Manual and Sedan
    elif answer.lower() == "manual" and response.lower() == "sedan":
        for index in range(2, 4):
            print(f"{modelYear[index]:<5}\t{manufacturer[index]:<10}\t{model[index]:<10}\t${price[index]:>5}")


    #Check conditions for Automatic and SUV
    elif answer.lower() == "automatic" and response.lower() == "suv":
        for index in range(4, 6):
             print(f"{modelYear[index]:<5}\t{manufacturer[index]:<10}\t{model[index]:<10}\t${price[index]:>5}")

    else:
        print("Vehicle Not Available")
    
            
    # Ask the user if they want to continue
    answer = input("Do you want to continue? (y/n): ")

