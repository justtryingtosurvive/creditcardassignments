from datetime import date

today = date.today()
todayString = str(today)
mm = todayString[5:7]
yy = todayString[2:4]

print("Mm = ", mm)
print("yy=",yy)