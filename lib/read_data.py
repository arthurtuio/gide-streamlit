import streamlit as st
import pandas as pd

from lib.requester import APIDataGetRequester
from lib.listas_de_valores_definidos import (
    db_tables_list,
    months_list,
    years_list,
    fornecedores_list,
    posto_list,
    modalidade_list,
    subgrupos_list
)


class ReadData:
    def execute(self):
        self.introduction()

    @staticmethod
    def introduction():
        st.markdown("""
            ## Consulta de registros ##
            
            Para realizar a consulta, primeiro selecione:
            
            1. A tabela de onde você quer selecionar os dados;
            2. Se você quer consultar todas as linhas ou deseja adicionar algum filtro;
            3. Se você quer consultar todas as colunas ou apenas algumas; # Será desenvolvido no futuro
        """)

        possible_row_filters_list = [
            "todas as linhas",
            "linhas filtradas por data"
        ]

        selected_table = st.selectbox(
            "Selecione a tabela:",
            db_tables_list()
        )

        if selected_table:
            selected_filter = st.selectbox(
                "Selecione agora o filtro para as linhas:",
                possible_row_filters_list
            )

            tarifas_other_query_params = None
            query_date = None

            if selected_filter == "linhas filtradas por data":
                query_date = _select_month_and_year_for_filter()

                if selected_table == "valor_tarifas":
                    if st.checkbox("Filtrar com mais parâmetros?"):
                        tarifas_other_query_params = _select_tarifas_params_for_filter()

            result_dataframe = pd.DataFrame(
                    APIDataGetRequester(
                        table=selected_table,
                        row_filter=selected_filter,
                        query_date=query_date,
                        tarifas_other_query_params=tarifas_other_query_params
                    )
                )

            st.markdown("** Resultado: **")
            st.dataframe(result_dataframe)


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
    ReadData().execute()
