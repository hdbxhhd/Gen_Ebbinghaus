import copy
from xx import genrate_date
from openpyxl import Workbook
a=[]
c=[" "]
num=int(input("Input how many parts do you divide your plan into?"))
start_time=int(input("Please input your start time:(such as 20200101, don't use 202011)"))
file_name=input("Enter the name of the file you want to create:")
file_name=file_name+".xlsx"
for i in range(1,num+1):
    b=[]
    b.append(i)
    a.append(copy.deepcopy(b))
for i in range(num):
    a[i]=[str(x) for x in a[i]]
for i in range(15):
    a.append(copy.deepcopy(c))
for i in range(num):
    a[i+1].append(str(i+1))
    a[i+2].append(str(i+1))
    a[i+4].append(str(i+1))
    a[i+7].append(str(i+1))
    a[i+15].append(str(i+1))

date=genrate_date(start_time,num)
for i in range(len(a)):
    a[i].insert(0,date[i])
list_name=["日期","学习","复习1","复习2","复习3","复习4","复习5"]
a.insert(0,list_name)
wb=Workbook()
sheet=wb.get_sheet_by_name("Sheet")

for i in range(len(a)):
    sheet.append(a[i])
wb.save(file_name)
