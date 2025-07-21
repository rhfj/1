list_1 = []
path = ""
dot = 0
count = -1
while not list_1:
    path = input("Введите путь к файлу: ")
    for i in range(len(path)):
        if path[i] == "\\":
         list_1.append(i)
        if path[i] == ".":
            dot = i
for i in list_1:
    count += 1
if count > -1:
    print(f"Имя файла: {path[list_1[count]+1:]}")
    print(f"Расширение файла: {path[dot+1:]}")
    print(f"Имя каталога: {path[list_1[0]+1:list_1[1]]}")
    print(f"Полный путь до каталога: {path[:list_1[count]+1]}")
