import streamlit as st
import matplotlib.pyplot as plt
choise = st.selectbox("укажите пол:", ["1 класс", "2 класс", "3 класс"])
data = {"мужчин:":0,"женщин:":0}
with open("data [1nzNjv].csv") as file:
    for line in file:
        d = line.split (',')
        gender = d[5]
        pclass = d[2]
        if choise == "1 класс" and pclass == '1':
            if gender == 'male':
                data ["мужчин:"] += 1
            else:
                data["женщин:"] += 1
        if choise == "2 класс" and pclass == '2':
            if gender == 'male':
                data["мужчин:"] += 1
            else:
                data["женщин:"] += 1
        if choise == "3 класс" and pclass == '3':
            if gender == 'male':
                data["мужчин:"] += 1
            else:
                data["женщин:"] += 1
st.dataframe(data)
fig = plt.figure(figsize=(10,5))
plt.bar(['мужчин','женщин'],[data["мужчин:"],data["женщин:"]])
st.pyplot(fig)