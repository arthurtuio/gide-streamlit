import streamlit as st
import pandas as pd
import numpy as np

from lib.read_data import ReadData
from lib.write_data import WriteData


class MainPage:
    def __init__(self):
        pass

    def execute(self):
        st.markdown("""
            # GIDE Main Web Page #
            
            Página criada com propósito de ser uma interface mais amigável
            do que a GIDE API, além de permitir a visualização de dashs dos
            dados e análises dos mesmos.

            Selecione no canto esquerdo a operação que você deseja realizar:
        
        _____________
        """)

        lista_operacoes = [
            "1. Consultar registros",
            "2. Inserir Registros",
            "3. Visualizar dados e análises (GIDE Dashboard)"
        ]

        operacao_selecionada = st.sidebar.selectbox("Operação escolhida", lista_operacoes)

        if operacao_selecionada == lista_operacoes[0]:
            ReadData().execute()

        elif operacao_selecionada == lista_operacoes[1]:
            WriteData().execute()

        elif operacao_selecionada == lista_operacoes[2]:
            pass


if __name__ == '__main__':
    MainPage().execute()