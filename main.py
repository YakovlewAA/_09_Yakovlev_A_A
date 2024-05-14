#импортируем необходимые для проекта библиотеки
import matplotlib.pyplot as plt
import streamlit as st

#подключаем файл с исходными данными
with open('data.csv') as file:
    #вводим переменные с пассажирами и билетами
    S_bilet = 0
    S_passenger = 0

    C_bilet = 0
    C_passenger = 0

    Q_bilet = 0
    Q_passenger = 0

    for line in file:
        data = line.split(',')

        #исключаем ID пассажира
        if data[0] == 'PassengerId':
            continue

        #высчитываем количество пассажиров с портом пасадки S и общую сумму стоимости билетов
        if data[12].strip() == 'S':
            S_passenger = S_passenger + 1
            S_bilet = S_bilet + float(data[10])

        # высчитываем количество пассажиров с портом пасадки С и общую сумму стоимости билетов
        if data[12].strip() == 'C':
            C_passenger = C_passenger + 1
            C_bilet = C_bilet + float(data[10])

        # высчитываем количество пассажиров с портом пасадки Q и общую сумму стоимости билетов
        if data[12].strip() == 'Q':
            Q_passenger = Q_passenger + 1
            Q_bilet = Q_bilet + float(data[10])

    #выводим print средней стоимости билета по портам посадки в стримлит (опционально закоментировано)
    #st.write("Средняя стоимость билета в порту посадки S:", round(S_bilet / S_passenger, 2))
    #st.write("Средняя стоимость билета в порту посадки C:", round(C_bilet / C_passenger, 2))
    #st.write("Средняя стоимость билета в порту посадки Q:", round(Q_bilet / Q_passenger, 2))

    #вводим переменные средней стоимости по портам посадки и присваиваем им значение из вычесления выше строчкой
    averageS = S_bilet / S_passenger
    averageC = C_bilet / C_passenger
    averageQ = Q_bilet / Q_passenger

    #minimumS
    #minimumC
    #minimumQ

#подключаем медиафал, заголовок и выподающий список из библиотеки стримлита
st.image('Titanic.jpg')
st.header('ПРАКТИЧЕСКОЕ ЗАНЯТИЕ №9. Яковлев А.А.')
st.write('Вычисление стоимости билета у пассажиров по каждому пункту посадки.')
option = st.selectbox('Выбирите категорию стоимости билета', ['Средняя', 'Минимальная', 'Максимальная'])
pport = ['Порт S', 'Порт C', 'Порт Q']

#если выбрана категория средней стоимости то переменная avg_port равна соответствующим переменным по портам посадки
if option == "Средняя":
    avg_port = [averageS, averageC, averageQ]

#if option == "Минимальная":
    #avg_port = [15.71, 18.22, 19.47]

#if option == "Максимальная":
    #avg_port = [122.13, 145.72, 144.28]

#avg_port = [27.08, 59.95, 13.28]

data = {'Порт посадки': pport, 'Cтоимость билета': avg_port}
st.table(data)

fig = plt.figure(figsize=(8, 3))
plt.bar(pport, avg_port)
plt.xlabel("Порт посадки")
plt.ylabel("Стоимость билета")
plt.title("Средняя стоимость по портам посадки")

st.pyplot(fig)