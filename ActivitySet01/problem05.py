def computepay(hours, rate):
    if hours >40:
        pay=(hours-40)*rate*1.5 +40* rate
    else:    
            pay=hours * rate
    return pay         
hours=int(input("enter hours:"))
rate=float(input("enter rate:"))
pay = computepay(hours, rate)
print("Pay",pay)
   

