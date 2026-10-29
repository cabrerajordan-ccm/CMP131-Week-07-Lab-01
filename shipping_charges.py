#Student name:Jordan Cabrera
#Course number:cmp 131
#Week number:7
#Lab number:1
#Assignment title:
#Date:10/28/26
weight=float(input("What is the weight in kilograms?"))
while weight<=0 or weight>=20:
    print("INVALID, please input a value bettween 0 and 20")
distance=int(input("What is the shipping distance in miles?"))  
while distance<10 or distance>3000:
    print("INVALID, please input a value bettween 10 and 300")
if weight<=2:
    rate=1.10
elif weight>2 and weight<=6:
    rate=2.20
elif weight>6 and weight<=10:
    rate=3.70
elif weight>10 and weight<=20:
    rate=4.80
miles=rate*500
charge=rate*(distance/500)
print("Package weight:",weight)
print("Shipping distance:",distance)
print("Rate per 500 miles:",rate)
print("Total shipping charge:",charge)