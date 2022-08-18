
import streamlit as st
import Controllers.ClienteController as ClienteController
import pandas as pd

def List():
    st.title("Cliente")
    costumerList = []

    for item in ClienteController.SelecionarTodos():
        costumerList.append([item.nome, item.idade, item.profissao])

    df = pd.DataFrame(
        costumerList,
        columns=['Nome', 'Idade', 'Profissão']
    )
    st.table(df)