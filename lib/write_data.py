import streamlit as st
import pandas as pd

from lib.requester import APIDataPostRequester
from lib.listas_de_valores_definidos import (
    db_tables_list,
    months_list,
    years_list,
    fornecedores_list,
    posto_list,
    modalidade_list,
    subgrupos_list
)


class WriteData:
    def execute(self):
        self._introduction()
        self._user_inputs()

    @staticmethod
    def _introduction():
        st.markdown("""
            ## Inserção de registros ##
            
            A única tabela que permite inserção de registros é a
            empresas_inputadas.
            
            **Nenhum dos valores deve ser adicionado com aspas!**
            
            Para entender qual o formato dos dados, selecione a checkbox abaixo:
        """)

        if st.checkbox("Conferir formato dos dados?"):
            st.markdown("""
                Ao adicionar uma linha, é obrigatório adicionar pelo menos estas colunas:
                - **data_referencia**: Ex: 08-09-2020 (DD-MM-YYYY)
                - **fornecedora**: Ex: CELESC
                - **unidade_consumidora**: Ex: 12812371234
                - **nome_cliente**: Ex: Autonomus Solucoes em Energia ( acentos e caracteres especiais)
                - **modalidade**: Ex: Basta escolher uma das opções da lista abaixo
                - **subgrupo**: Ex: Basta escolher uma das opções da lista abaixo
                - **consumo_ponta**: Ex:
                - **consumo_fora_ponta**: Ex:
                - **demanda_medida_ponta**: Ex:
                - **demanda_medida_fora_ponta**: Ex:
                
                Estas outras colunas abaixo são opcionais. Para inserir valores para elas, selecione a opção
                "Adicionar também colunas opcionais?". Abaixo uma descrição das mesmas, seguido
                dos valores padrão que elas vem (caso não seja selecionada a opção), e um exemplo de dado das mesmas:
                - **demanda_contratada_ponta**: Valor Padrão: 0 Ex: 240 (sem virgula/ponto)
                - **demanda_contratada_fora_ponta**: Valor Padrão: Ex: 440 (sem virgula/ponto)
                
                - **is_teste_ponta**: Valor Padrão: False Ex: True
                - **is_teste_fora_ponta**: Valor Padrão: False Ex: True
                
                - **geracao_ener_ponta**: Valor Padrão: 0 False Ex: 2345.12 (com virgula/ponto)
                - **geracao_ener_fora_ponta**: Valor Padrão: 0 False Ex: 2341.0 (com virgula/ponto)
                
                - **ener_reat_exced_ponta**: Valor Padrão: 0 Ex: 240 (sem virgula/ponto)
                - **ener_reat_exced_fora_ponta**: Valor Padrão: 0 Ex: 240 (sem virgula/ponto)
                
                - **demanda_reat_exced_ponta**: Valor Padrão: 0 Ex: 240 (sem virgula/ponto)
                - **demanda_reat_exced_fora_ponta**: Valor Padrão: 0 Ex: 240 (sem virgula/ponto)
            """)

    @staticmethod
    def _user_inputs():
        st.markdown("""
            ____________
            
            **Por favor, selecione a opção de adição de dados:**
            
            Note que se for em CSV, os dados devem seguir a mesma
            lógica de formatação de dados.
        """)

        insertion_methods = ["Inserindo por aqui", "CSV"]

        selected_method = st.selectbox(
            "Como você irá adicionar seus dados?",
            insertion_methods
        )

        if selected_method == insertion_methods[0]:
            user_inputted_data = _get_user_inputs_streamlit()

            if st.checkbox("Adicionar também colunas opcionais?"):
                user_inputted_optional_data = _get_user_optional_inputs_streamlit()
                st.markdown("** A parte de parametros opcionais será desenvolvida no futuro **")

            st.markdown("""
                Assim que você ter apertado Enter pra cada um
                dos dados digitados acima, só apertar esse botão
                para inserir:

                ** Cada clique insere 1 registro!! **
            """)

            if st.button("Inserir dados!"):
                response = APIDataPostRequester(user_inputted_data=user_inputted_data)
                st.markdown(response)

        else:
            st.markdown("** A inserção por CSV ainda será desenvolvida **")


def _get_user_inputs_streamlit():
    data_referencia = st.text_input("data_referencia:")
    fornecedora = st.text_input("fornecedora:")
    unidade_consumidora = st.text_input("unidade_consumidora:")
    nome_cliente = st.text_input("nome_cliente:")
    modalidade = st.text_input("modalidade:")
    subgrupo = st.text_input("subgrupo:")
    consumo_ponta = st.text_input("consumo_ponta:")
    consumo_fora_ponta = st.text_input("consumo_fora_ponta:")
    demanda_medida_ponta = st.text_input("demanda_medida_ponta:")
    demanda_medida_fora_ponta = st.text_input("demanda_medida_fora_ponta:")

    return {
        "data_referencia": data_referencia,
        "fornecedora": fornecedora,
        "unidade_consumidora": unidade_consumidora,
        "nome_cliente": nome_cliente,
        "modalidade": modalidade,
        "subgrupo": subgrupo,
        "consumo_ponta": consumo_ponta,
        "consumo_fora_ponta": consumo_fora_ponta,
        "demanda_medida_ponta": demanda_medida_ponta,
        "demanda_medida_fora_ponta": demanda_medida_fora_ponta,
    }


def _get_user_optional_inputs_streamlit():
    return None


def _select_month_and_year_for_filter():
    selected_month = st.selectbox(
        "Selecione o mês para o filtro de data:",
        months_list()
    )

    selected_year = st.selectbox(
        "Selecione o ano para o filtro de data:",
        years_list()
    )

    return str(f'01-{selected_month}-{selected_year}')


def _select_tarifas_params_for_filter():
    selected_fornecedor = st.selectbox(
        "Selecione a Fornecedora:",
        fornecedores_list()
    )

    selected_posto = st.selectbox(
        "Selecione o Posto:",
        posto_list()
    )

    selected_modalidade = st.selectbox(
        "Selecione a modalidade:",
        modalidade_list()
    )

    selected_subgrupo = st.selectbox(
        "Selecione o subgrupo:",
        subgrupos_list()
    )

    return {
        "fornecedora": selected_fornecedor,
        "selected_posto": selected_posto,
        "selected_modalidade": selected_modalidade,
        "selected_subgrupo": selected_subgrupo,
    }


if __name__ == '__main__':
    WriteData().execute()
