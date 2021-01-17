def check_year(year):
    return year%400==0 or (year%4==0 and year%100!=0)
def genrate_date(start_time,times):
    a=[]
    year=start_time//10000
    month=(start_time%10000)//100
    day=(start_time%10000)%100
    for i in range(times+15):
        a.append(str(year*10000+month*100+day))
        if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            if(day==31):
                if(month==12):
                    day=1
                    month=1
                    year=year+1
                else:
                    month=month+1
                    day=1
            else:
                day=day+1
        elif(month==4 or month==6 or month==9 or month==11):
            if(day==30):
                month=month+1
                day=1
            else:
                day=day+1
        elif(month==2):
            if(check_year(year)):#闰年
                if(day==29):
                    day=1
                    month=3
                else:
                    day=day+1
            else:
                if(day==28):
                    day=1
                    month=3
                else:
                    day=day+1
    return a

# print(genrate_date(20210117,40))