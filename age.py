#EX1
age = int(input("enter your age: "))
if age < 10:
    print("price is 10$" )
elif 10 <= age <18:
    print ("price is 15$" )
elif 18<= age < 70:
    print("price is 20$" )
else:
    print("price is 25$ ")
