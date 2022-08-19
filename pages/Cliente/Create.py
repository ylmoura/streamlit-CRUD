import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente


def IncluirClientePage():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        st.write(idAlteracao)
        st.write(idAlteracao)
        st.title("Alterar cliente")
    else:
        st.title("Cliente")
    with st.form(key="include_cliente"):
        input_name = st.text_input(label="insira o seu nome")
        input_age = st.number_input(label="Insira sua idade", format="%d",step=1)
        input_occupation = st.selectbox("selecione sua profissão", ["desenvolverdor","Músico","Professor"])
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        ClienteController.Incluir(cliente(0, input_name, input_age, input_occupation))
        st.success("Cliente incluido com sucesso!")