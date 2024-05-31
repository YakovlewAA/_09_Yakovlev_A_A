# import streamlit as st


def  get_bilet(lines):


    S_bilet=0
    S_passajir=0
    S_min = -1
    S_max = 0

    C_bilet = 0
    C_passajir = 0
    C_min = -1
    C_max = 0

    Q_bilet = 0
    Q_passajir = 0
    Q_min = -1
    Q_max = 0

    for line in lines:
        data = line.split(',')

        if data[0] == 'PassengerId':
            print(data[10])
            continue    #переход на следую строку
        if data[10] == '' or data[10] == ' ':
            continue  # Пропускаем пассажира без стоимости билета

        if data[12].strip() == 'S':     #strip убирает переход - enter
            S_passajir = S_passajir + 1
            S_bilet = S_bilet + float(data[10])

            if (S_min > float(data[10]) or S_min == -1) and float(data[10]) != 0:
                S_min = float(data[10])
            if S_max < float(data[10]):
                S_max = float(data[10])

        if data[12].strip() == 'C':     #strip убирает переход - enter
            C_passajir = C_passajir + 1
            C_bilet = C_bilet + float(data[10])

            if (C_min > float(data[10]) or C_min == -1) and float(data[10]) != 0:
                C_min = float(data[10])
            if C_max < float(data[10]):
                C_max = float(data[10])

        if data[12].strip() == 'Q':     #strip убирает переход - enter
            Q_passajir = Q_passajir + 1
            Q_bilet = Q_bilet + float(data[10])

            if (Q_min > float(data[10]) or Q_min == -1) and float(data[10]) != 0:
                Q_min = float(data[10])
            if Q_max < float(data[10]):
                Q_max = float(data[10])
    return S_bilet, S_passajir, S_min, S_max, C_bilet, C_passajir, C_min, C_max, Q_bilet, Q_passajir, Q_min, Q_max





with open("data.csv") as file:
   lines = file.readlines()
   S_bilet, S_passajir, S_min, S_max, C_bilet, C_passajir, C_min, C_max, Q_bilet, Q_passajir, Q_min, Q_max = get_bilet(lines)





print("Средняя стоимость билета в порту посадки S:",  round(S_bilet / S_passajir,2))
print("Минимальная стоимость билета в порту посадки S:",  round(S_min,2))
print("Максимальная стоимость билета в порту посадки S:",  round(S_max,2))

print()

print("Средняя стоимость билета в порту посадки C:",  round(C_bilet / C_passajir,2))
print("Минимальная стоимость билета в порту посадки C:",  round(C_min,2))
print("Максимальная стоимость билета в порту посадки C:",  round(C_max,2))

print()

print("Средняя стоимость билета в порту посадки Q:",  round(Q_bilet / Q_passajir,2))
print("Минимальная стоимость билета в порту посадки Q:",  round(Q_min,2))
print("Максимальная стоимость билета в порту посадки Q:",  round(Q_max,2))






