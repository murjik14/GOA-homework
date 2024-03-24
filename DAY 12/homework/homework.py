
# ფუნქცია, რომელიც შეუზღუდავს თქვენს სასურველ პაროლს

def check_password():
    correct_password = input("შეიყვანეთ სასურველი პაროლი: ")
    attempts = 0
    while True:
        password = input("შეიყვანეთ პაროლი: ")
        if password == correct_password:
            print("პაროლი სწორია!")
            break
        else:
            attempts += 1
            if attempts >= 5:
                print("სისტემა დაბლოკილია!")
                break
            else:
                print("პაროლი "" არასწორია, სცადეთ თავიდან.")

# ფუნქცია, რომელიც გამოიყენებს for ციკლს მინიმალური და მაქსიმალური მნიშვნელობების სასწავლებლად
                
def learn_for_loop():
    minimum = int(input("შეიყვანეთ მინიმალური მნიშვნელობა: "))
    maximum = int(input("შეიყვანეთ მაქსიმალური მნიშვნელობა: "))
    step = int(input("შეიყვანეთ სტეპი: "))
    print("for ციკლის სასწავლებლად:")
    for i in range(minimum, maximum + 1, step):
        print(i)

# ფუნქცია, რომელიც გამოიყენებს while ციკლს გვერდების შემოწმებისთვის
        
def check_pages():
    page = int(input("შეიყვანეთ სამკუთხედის სამი გვერდი: "))
    while page < 1 or page > 3:
        print("არასწორი გვერდი, სცადეთ თავიდან.")
        page = int(input("შეიყვანეთ სამკუთხედის სამი გვერდი: "))
    print("გვერდი სწორია.")

# ფუნქცია, რომელიც ხარისხის შემოწმებისთვის გამოიყენებს if-else მიმართულებას
    
def check_quality():
    grade = int(input("შეიყვანეთ ხარისხი: "))
    if grade >= 60:
        print("ხარისხი მართია.")
    else:
        print("ხარისხი არასწორია.")

# ფუნქცია


def calculate_hypotenuse():
    side1 = float(input("შეიყვანეთ მართკუთხას პირველი კათეტი: "))
    side2 = float(input("შეიყვანეთ მართკუთხას მეორე კათეტი: "))
    hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
    print("ჰიპოტენუზა არის:", hypotenuse)

# ფუნქცია, რომელიც წელის სამი შემოწმების შემდეგ დააბეჭდავს შედეგს
def check_age():
    age = int(input("შეიყვანეთ წელი: "))
    if age >= 18 and age <= 65:
        print("თქვენ შეგიძლიათ მონაწილეობა.")
    else:
        print("თქვენ არ შეგიძლიათ მონაწილეობა.")

# პროგრამის მთავარი ნაწილი
def main():
    operation = input("ოპერაცია (+, -, *, /): ")
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

    if operation == '+':
        print("შედეგია:", num1 + num2)
    elif operation == '-':
        print("შედეგია:", num1 - num2)
    elif operation == '*':
        print("შედეგია:", num1 * num2)
    elif operation == '/':
        if num2 != 0:
            print("შედეგია:", num1 / num2)
        else:
            print("გამყიდველი შეცდომა: ნულზე გაყოფა არ შეგიძლია.")

    check_password()
    learn_for_loop()
    check_pages()
    check_quality()
    calculate_hypotenuse()
    check_age()

# პროგრამის გაშვება
if __name__ == "__main__":
    main()
