def interest(principal,rate,time):
    i=principal*(1+(rate*time))
    print "intrest for given values :",i
    return

p=input("enter value of principal :")
r=input("enter value of rate :")
t=input("enter value of time :")
interest(p,r,t)
