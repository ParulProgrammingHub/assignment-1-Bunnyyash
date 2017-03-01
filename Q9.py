sub=[]
s=0
for i in range(5):
    m=input("enter mark of subject out of 50:")
    sub.append(m)
    s=float((s+sub[i]))
mean=s/5
print "Mean :",mean
per=float(s/250)*100
print "you have scored %d PERCENTAGE" %per
if(per<35):
    print("Sorry you have failed ")
else:
    print("Congratulations you have passed")

    
