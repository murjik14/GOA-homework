

1.# AND ოპერატორი:

x = 5
y = 10
z = 15

if x < y and y < z:
    print("Both conditions are true")
else:
    print("At least one condition is false")


2. #OR ოპერატორი:

x = 5
y = 10

if x > 3 or y < 5:
    print("At least one condition is true")
else:
    print("Both conditions are false")

3. #AND-OR ოპერატორები:
x = 5
y = 10
z = 15

if x < y and y < z or x == 5:
    print("At least one condition is true")
else:
    print("All conditions are false")


4. #OR-AND ოპერატორები:

x = 5
y = 10
z = 15

if x > y or y < z and z == 15:
    print("At least one condition is true")
else:
    print("All conditions are false")


5.# NOT ოპერატორი:

x = 5

if not x == 10:
    print("x is not equal to 10")
else:
    print("x is equal to 10")

6. #AND-NOT ოპერატორი:

x = 5
y = 10

if x < y and not y == 10:
    print("y is not equal to 10 and x is less than y")
else:
    print("Either y is equal to 10 or x is not less than y")


7. #OR-NOT ოპერატორი:

x = 5
y = 10

if x == 5 or not y == 10:
    print("Either x is equal to 5 or y is not equal to 10")
else:
    print("Neither x is equal to 5 nor y is not equal to 10")


8. #AND-OR-NOT ოპერატორი:

x = 5
y = 10
z = 15

if x < y and y < z or not x == 5:
    print("At least one condition is true")
else:
    print("All conditions are false")


9. #OR-AND-NOT ოპერატორი:

x = 5
y = 10
z = 15

if x > y or y < z and not z == 15:
    print("At least one condition is true")
else:
    print("All conditions are false")


10. #კომბინაცია მრავალისა და NOT ოპერატორების:

x = 5
y = 10
z = 15

if (x < y or y < z) and not (x == 5 and z == 15):
    print("At least one condition is true and both x and z are not equal to their respective values")
else:
    print("All conditions are false or both x and z are equal to their respective values")
