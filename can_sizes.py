import math
import csv

database = open("canDatabase.csv","r")
def main():
    radiusList = []
    heightList = []
    nameList = []
    index = 0
    
    with database as csv_file:
        for row_list in csv.reader(csv_file):
            nameList.append(row_list[0])
            radiusList.append(float(row_list[1]))
            heightList.append(float(row_list[2]))
        
            #this is a thing ---v
            print(f"The efficiency score of {nameList[index]} is {storage_efficiency(radiusList[index],heightList[index]):.2f}")
            index+=1

def storage_efficiency(radius, height):
    #this is maths for storage efficency--v
    return (math.pi*radius*radius*height)/(2*math.pi*radius*(radius+height))

main()