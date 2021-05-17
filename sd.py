import math
import csv

with open ("data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]

#step1: finding mean
def mean (data):
    n = len(data)
    total = 0
    for x in data :
        total += int(x)
    mean = total/n
    return mean

#step2 : squaring and getting the values
squared_list = []
for number in data:
    a = int(number)- mean(data)
    a = a ** 2
    squared_list.append(a)

#step 3 : getting the sum of the squares
sum = 0 
for i in squared_list:
    sum = sum+i

#step 4 : divide the sum by the total values
result = sum/(len(data)-1)

#step 5 :finding the square root of the values- to find sd
std_deviation = math.sqrt(result)
print("standard deviation is ==>", std_deviation)