
# დავალება 1
numbers_1 = list(range(21))
print("დავალება 1:", numbers_1)

# დავალება 2
num1 = int(input("შემოიტანეთ პირველი რიცხვი: "))
num2 = int(input("შემოიტანეთ მეორე რიცხვი: "))
print("დავალება 2: არსებულები:", num1, num2)

# დავალება 3
numbers_2 = list(range(50, 101))
print("დავალება 3:", numbers_2)

# დავალება 4
numbers_3 = list(range(100, 49, -1))
print("დავალება 4:", numbers_3)

# დავალება 5
numbers_4 = list(range(51))
print("დავალება 5: რიცხვები:", numbers_4)
print("დავალება 5: ბოლოს ჯამი:", sum(numbers_4))

# დავალება 6
num3 = int(input("შემოიტანეთ რიცხვი: "))
numbers_5 = list(range(num3 + 1))
print("დავალება 6: ყველა მთელი რიცხვი 0-დან", num3, "მდე:", numbers_5)

# დავალება 7
age = int(input("შემოიტანეთ ასაკი: "))
age_after_10_years = age + 10
print("დავალება 7: ასაკი:", age, "10 წლის შემდეგ:", age_after_10_years)
