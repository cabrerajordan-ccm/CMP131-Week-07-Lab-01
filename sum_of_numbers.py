#Student name:Jordan Cabrera
#Course number:cmp 131
#Week number:7
#Lab number:1
#Assignment title:sum_of_numbers
#Date:10/28/26
start_number=int(input("Enter a positive integer:"))
while start_number<=0:
    print("Error:Please enter a number greater than zero")
    start_number=int(input("Enter a positive integer:"))
sum=0
current_num=1
while current_num<= start_number:
    sum+=current_num
    current_num+=1
print("The sum of integers from 1 to",start_number, "is", sum)
