# დავიწყოთ `math` მოდულის იმპორტი:

import math


1. # რიცხვების ჯამი
num1 = 10
num2 = 20
sum_result = num1 + num2
print("რიცხვების ჯამი:", sum_result)

# რიცხვების ნამრავლი
multiply_result = num1 * num2
print("რიცხვების ნამრავლი:", multiply_result)

2. # კვადრატის გამოთვლა
num = 9
square_result = math.sqrt(num)
print("კვადრატული ფუნქციით მიღებული შედეგი:", square_result)

# ფუნქციის გამოყენება ციკლში
for i in range(1, 11):
    print(i, " რიცხვის კვადრატი:", math.sqrt(i))


3. # ცელსიუსიდან ფარენგეიტში გარდაქმნა
celsius = 37.5
fahrenheit = (celsius * 9/5) + 32
print("ცელსიუსიდან ფარენგეიტში:", fahrenheit)

# ფუნქციის გამოყენება ციკლში
for temp in range(0, 101, 10):
    celsius = temp
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, " ცელსიუსი =", fahrenheit, " ფარენგეიტი")


4. # მნიშვნელობის შემთხვევა
num = -5
abs_value = abs(num)
print("მნიშვნელობის შემთხვევა:", abs_value)


5. # ფაქტორიალი
number = 5
factorial = math.factorial(number)
print("ფაქტორიალი:", factorial)
