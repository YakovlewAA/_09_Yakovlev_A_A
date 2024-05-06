import matplotlib.pyplot as plt
import streamlit as st

st.image('Titanic.jpg')
st.header('ПРАКТИЧЕСКОЕ ЗАНЯТИЕ №9. Яковлев А.А.')
st.write('Вычисление средней стоимости билета у пассажиров по каждому пункту посадки.')
st.selectbox('Средняя стоимость билета в порту посадки', ['Порт S', 'Порт C', 'Порт Q'])
pport = ['Порт S', 'Порт C', 'Порт Q']
avg_port = [27.08, 59.95, 13.28]
data = {'Порт посадки': pport, 'Средняя стоимость билета': avg_port}
st.table(data)

fig = plt.figure(figsize=(8, 3))
plt.bar(pport, avg_port)
plt.xlabel("Порт посадки")
plt.ylabel("Стоимость билета")
plt.title("Средняя стоимость по портам посадки")

st.pyplot(fig)