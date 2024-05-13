import matplotlib.pyplot as plt
import streamlit as st

st.image('Titanic.jpg')
st.header('ПРАКТИЧЕСКОЕ ЗАНЯТИЕ №9. Яковлев А.А.')
st.write('Вычисление средней стоимости билета у пассажиров по каждому пункту посадки.')
option = st.selectbox('Стоимость билета в порту посадки', ['Средняя', 'Минимальная', 'Максимальная'])
pport = ['Порт S', 'Порт C', 'Порт Q']

if option == "Средняя":
    avg_port = [27.08, 59.95, 13.28]

if option == "Минимальная":
    avg_port = [15.71, 18.22, 19.47]

if option == "Максимальная":
    avg_port = [122.13, 145.72, 144.28]

#avg_port = [27.08, 59.95, 13.28]
data = {'Порт посадки': pport, 'Cтоимость билета': avg_port}
st.table(data)

fig = plt.figure(figsize=(8, 3))
plt.bar(pport, avg_port)
plt.xlabel("Порт посадки")
plt.ylabel("Стоимость билета")
plt.title("Средняя стоимость по портам посадки")

st.pyplot(fig)