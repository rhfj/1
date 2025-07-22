password = input("Введите пароль: ")
count_up = 0
count_digit = 0
count_low = 0
count_sign = 0
for i in range(len(password)):
    if password[i] == " ":
        print("Неккоректный пароль!")
    elif password[i].isupper():
        count_up += 1
    elif password[i].isdigit():
        count_digit += 1
    elif password[i].islower():
        count_low += 1
    else:
        count_sign += 1
if count_up > 0 and count_low > 0 and (count_digit > 0 or count_sign > 0) and len(password) > 5:
    print("Пароль корректный!")
else:
    print("Пароль некорректный!")
