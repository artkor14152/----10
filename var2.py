import streamlit as st
import matplotlib.pyplot as plt


def getinfo(lines, opt):
    survived = 0
    notSurvived = 0
    for line in lines:
        data = line.split(",")
        isSurvived = data[1]
        port = data[12].strip()
        if port == "C" and opt == "Шербур":
            if isSurvived == "1":
                survived += 1
            else:
                notSurvived += 1
        if port == "Q" and opt == "Квинстоун":
            if isSurvived == "1":
                survived += 1
            else:
                notSurvived += 1
        if port == "S" and opt == "Саутгемптон":
            if isSurvived == "1":
                survived += 1
            else:
                notSurvived += 1
    return survived, notSurvived


def var2():
    st.title('Подсчитать число спасенных и погибших для указанного пункта посадки.')
    option = st.selectbox("Выбирете пункт посадки ", ["Шербур", "Квинстоун", "Саутгемптон"])
    with open("data.csv") as f:
        next(f)
        survived, notSurvived = getinfo(f.readlines(), option)
        if option == "Шербур":
            st.table({"Спасённых": survived, "Погибших": notSurvived})
            fig = plt.figure(figsize=(10, 5))
            plt.xlabel("Значение поля Survived")
            plt.ylabel("Количество")
            plt.title("Количество спасённых и погибших в Шербуре")
            plt.bar(["Спасённых", "Погибших"], [survived, notSurvived])
            st.pyplot(fig)
        elif option == "Квинстоун":
            st.table({"Спасённых": survived, "Погибших": notSurvived})
            fig = plt.figure(figsize=(10, 5))
            plt.xlabel("Значение поля Survived")
            plt.ylabel("Количество")
            plt.title("Количество спасённых и погибших в Квинстоуне")
            plt.bar(["Спасённых", "Погибших"], [survived, notSurvived])
            st.pyplot(fig)
        elif option == "Саутгемптон":
            st.table({"Спасённых": survived, "Погибших": notSurvived})
            fig = plt.figure(figsize=(10, 5))
            plt.xlabel("Значение поля Survived")
            plt.ylabel("Количество")
            plt.title("Количество спасённых и погибших в Саутгемптоне")
            plt.bar(["Спасённых", "Погибших"], [survived, notSurvived])
            st.pyplot(fig)
