words = ""
result = ""
list_1 = []
while not list_1:
    words = input("Введите череду цифер и одинарных ковычек: ")
    for i in range(len(words)):
     if words[i] == "\'":
        list_1.append(i)
for i in range(len(words)):
    if words[i] != "\'":
        result += words[i]
print(int(result))
