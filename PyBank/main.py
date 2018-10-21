import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')


with open(budget_csv, 'r') as csvfile:
  
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csvdata = list (csvreader) 

    trimmed = csvdata[1:]
    #print(trimmed)
    
    TotalDates = len(trimmed)
    print(TotalDates)

    NetProfit = [int(i[1]) for i in trimmed]
    #print(NetProfit)

    SumNetProfit = sum(list(NetProfit))   
    print(SumNetProfit)

    MaxProfit = max(list(NetProfit))
    print (MaxProfit)

    MinProfit = min(list(NetProfit))
    print(MinProfit)
    
  
    






    




