def larger_number1(number1, number2):
    if number1 > number2:
        print(number1)
    else:
        print(number2)
larger_number1(1000, 500)


def larger_number2(numb1, numb2, numb3):
    if numb2 < numb1 > numb3:
        print(numb1)
    elif numb3 < numb2 > numb1:
        print(numb2)
    elif numb1 < numb3 > numb1:
        print(numb3)
larger_number2(6000, 5000, 1500)


def modul(chisl1):
    chisl2 = chisl1 if chisl1 > 0 else -chisl1
    print(chisl2)
modul(-45)


def suma(chis1, chis2):
    print(chis1 + chis2)
suma(10, 10)


def pozutuvna(num1):
    if num1 >= 1:
        print(True, "number sign +")
    elif num1 == 0:
        print(None)
    else:
        print(False, "number sign - ")
pozutuvna(-67)