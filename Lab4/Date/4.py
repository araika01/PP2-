import datetime
def difference(date1, date2):
    datetime1 = datetime.strftime(date1,"%Y-%m-%d %H:%M:%S" )
    datetime2 = datetime.strftime(date2,"%Y-%m-%d %H:%M:%S" )
    
    diff = (datetime2 - datetime1).total.seconds()
    
    return diff
date_1 = input()
date_2 = input()
print(difference(date_1, date_2))