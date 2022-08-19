import unittest
from warnings import catch_warnings import main
import streamlit as st
import Controllers.ClienteController as ClienteController
import pages.Cliente.Create as PagesCreateCliente

def List():
# st.title("Cliente")
 #   costumerList = []

  #  for item in ClienteController.SelecionarTodos():
   #     costumerList.append([item.nome, item.idade, item.profissao])

    #df = pd.DataFrame(
     #   costumerList,
      #  columns=['Nome', 'Idade', 'Profissão']
    #)
    #st.table(df) 
    paramId = st.experimental_get_query_params()
    if paramId == {}:
        colms = st.columns((1, 2, 1, 2, 1, 1))
        campos = ['Nª','Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms,campos):
            col.write(campo_nome)
        for item in ClienteController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1, 1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            button_space_excluir = col5.empty()
            on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' + str(item.id))


            if on_click_excluir:
                ClienteController.Excluir(item.id)
                button_space_excluir.button('Excluído','btnExcluir' + str(item.id)) 

            if on_click_alterar:
                st.experimental_get_query_params(
                    id = [item.id]
                )     
                st.experimental_rerun()
    else:
        PagesCreateCliente.Create()




