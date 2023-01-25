import math
import csv
from datetime import datetime

# Instantiate Files and lists
file1 = open("volumes.txt", "a")
widthList = []
aspectList = []
diameterList = []
volumeList = []
priceList = []

# Get input from user for width, AR, and wheel diameter:
width = int(input("Please enter the width of the tire in mm: "))
aspectRatio = input("Please enter the aspect ratio of the tire: ")
formatter = "r"
if formatter in aspectRatio:
    aspectRatio = aspectRatio.replace("r", "")
aspectRatio = float(aspectRatio)
wheelDiameter = float(input("Please enter the wheel diameter in inches that the tire should fit: "))


# Calculates the volume in liters and formats it
vol = (math.pi * (width ** 2)*aspectRatio*((width*aspectRatio)+2540*wheelDiameter))/(10 ** 10)
volume = float(f"{vol:.2f}")

# Create a list of the data that was input by user.
specifications = [str(width),str(aspectRatio),str(wheelDiameter),str(volume)]


#Saves data to a file, and gives it a time stamp.
file1.write(f"Date: {datetime.now():%Y-%m-%d}, Width: {width}, AspectRatio: {aspectRatio}, WheelDiameter: {wheelDiameter}, Volume: {volume}\n")


# Gives the User back the volume of the tire
print(f"The volume of the tire in question is {volume: .2f} liters.")


# Asks if the user would like an estimate on tires
if input("Would you like an estimate for the cost of your tires? (y/n) ")=="y":
    
    def main():
        # Open the CSV file for reading and store a reference
        # to the opened file in a variable named csv_file.
        with open("data.csv", "rt") as csv_file:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)

            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:
                # print(row_list)
                # Retrieve the values as lists
                widthList.append(row_list[0])
                aspectList.append(row_list[1])
                diameterList.append(row_list[2])
                volumeList.append(row_list[3])
                priceList.append(row_list[4])
    # Call main to start this program.
    if __name__ == "__main__":
        main()

    # Searches the database to find if there is a matching tire and price.
    i = 0
    checkAvailable = False
    for each in priceList:
        if specifications[0]==widthList[i] and specifications[1]==aspectList[i] and specifications[2]==diameterList[i]:
            print(f"we have that tire available for ${priceList[i]}")
            checkAvailable = True
            
        i = i+1

    # Gets the User to record their phone number in order to purchase tires, if any are available.
    if checkAvailable:
        phoneL = 0       
        if input("Would you like to buy tires for the specified dimensions? (y/n) ")=="y":
            while phoneL !=10:
                phone = input("Please enter your phone number: ")
                phoneL = len(phone)

        file1.write(f"Phone Number: {phone}\n")
        print("Thank you for your phone number.")
    else:
        print("\033[1;32m Error: Cannot find price for specified tire in database.")



"""
I believe my Program meets the "Exceeds Requirements" criteria. I have added a few features to make the experience more
user-friendly, and the code easy to read, as well as a feature for purchasing the tires that registers a phone number.

Google Drive link to the data.csv:
https://drive.google.com/drive/folders/1y5G0jQ4emcrOjY60J3ykCIp8DjpiOoCm?usp=sharing
"""