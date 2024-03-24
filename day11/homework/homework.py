#5-ის ჯერადების ბეჭდვა 1-დან 50-ის ჩათვლით for loop-ის გამოყენებით:

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#ლუწი რიცხვების ბეჭდვა 2-დან 20-ის ჩათვლით for loop-ის გამოყენებით:
        
for i in range(2, 21):
    if i % 2 == 0:
        print(i)

#5-დან ათამდე რიცხვების ნამრავლის ბეჭდვა for loop-ის გამოყენებით:
        
        result = 1
for i in range(5, 11):
    result *= i
print(result)

#რიცხვის ფაქტორიალის გათიშვა for loop-ის გამოყენებით:

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("შეიყვანეთ რიცხვი: "))
print("ფაქტორიალი:", factorial(number))

#შემოტანილი რიცხვის ლუწობის და გაყავის ან გამრავლების გათიშვა:

number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    result = number // 2
else:
    result = number * 3 + 1

print("შედეგი:", result)

