days=input("enter the nos. of days")
year=days/360
temp=days%360

month=temp/30
day=temp%30
print "nos. of year %d months %d days %d" %(year,month,day)
n=raw_input("press any key to exit")
