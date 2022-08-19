from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import Controllers.ClienteController as ClienteController
import pandas as pd
import pages.Cliente.Create as PageCreateCliente
import pages.Cliente.List as PageListCliente




st.sidebar.title('Menu')
Page_cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Consultar'])

if Page_cliente == 'Consultar':
    PageListCliente.List()
if Page_cliente == 'Incluir':
    PageCreateCliente.IncluirClientePage()


