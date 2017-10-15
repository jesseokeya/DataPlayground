import numpy as np
import csv as csv

def main():
   readdata = csv.reader(open('../resources/bankData.csv'))
   data = []
   trackDataKeys = {}

   for row in readdata:
       data.append(row)

   for i in range(len(data[0])):
       trackDataKeys[data[0][i]] = []

   print(trackDataKeys)
   print(data[0][0])
   data.pop(0)

   for i in range(len(data)):
       for j in range(len(data[i])):
           if j < len(trackDataKeys):
             print(j)




   # for i in range(len(data)):
   #     for j in range(len(data[i])):
   #         print(data[i][j])




main()
