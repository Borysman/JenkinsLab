if __name__ == '__main__':

    def openf(name="text.txt"):  # запис файлу у список
        try:
            file, lst = list(open(name, "r", encoding='utf-8')), []
            lst = file[0].split(", ")
            return lst
        except FileNotFoundError:
            return False

    def saving(lst):  # збереження файлу
        f = open('text.txt', "w")
        f.write(', '.join(str(value) for value in lst))

    def show(lst):  # показ списку користувачеві
        return ', '.join(str(value) for value in lst)


    def maxrnge(lst):
        if len(lst) >= 10:
            return False
        else:
            return True

    def minrnge(lst):
        if len(lst) <= 0:
            return False
        else:
            return True

    def ifexits(lst, a):
        if lst.count(a) < 1:
            return True
        else:
            return False

    if __name__ == '__main__':
        lst = (openf())
        if lst == False:
            lst = ["Valentyn", "Maksym"]
        while True:
            print("\n-----------------------------------------------------\n")
            print("Теперішній стан черги: \n", show(lst))
            dia = input("Введіть дію (1 - додати в кінець черги, 2 - показати першого в черзі, 3 - видалити першого, 0 - зберегти стан черги): ")
            if dia == "1":
                if maxrnge(lst):
                    inf = input("Введіть Кого додати: ")
                    if ifexits(lst, inf):
                        lst.append(inf)
                    else:
                        print("\nТака людина вже в черзі\n")
                else:
                    print("\nЧерга вже повна\n")
            elif dia == "2":
                if minrnge(lst):
                    print("\n3араз черга: ", lst[0])
                else:
                    print("\nЧерга пуста\n")
            elif dia == "3":
                if minrnge(lst):
                    print("Видаляю: ", lst.pop(0))
                else:
                    print("\nЧерга вже пуста\n")
            elif dia == "0":
                print("\nФайл збережено")
                saving(lst)

