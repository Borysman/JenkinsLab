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

def show(lst):  # показ списку користувачеві
    return ', '.join(str(value) for value in lst)

if __name__ == '__main__':

    lst = ["106", "107"]
    while True:
        print("\n-----------------------------------------------------\n")
        print("Теперішній стан черги: \n", show(lst))
        dia = input("Введіть дію (1 - додати замовлення в кінець черги, 2 - показати замовлення перше в черзі, 3 - завершити виконання першого замовлення): ")
        if dia == "1":
            if maxrnge(lst):
                inf = input("Введіть номер замовлення: ")
                if ifexits(lst, inf):
                    lst.append(inf)
                else:
                    print("\nТаке замовлення вже в черзі\n")
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

