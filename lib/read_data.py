import streamlit as st
import pandas as pd

from lib.requester import APIDataRequester


def get_API_data(table, row_filter, columns=None):
    """
    Dar um jeito de salvar na memória algo, pra n ficar consultando INFINITO do banco de dados
    :param table:
    :param row_filter:
    :param columns:
    :return:
    """
    return APIDataRequester(table, row_filter)


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

        tables_list = [
            "empresas_valores_inputados",
            "valor_tarifas",
            "valor_bandeiras",
            "valor_impostos",
        ]

        possible_row_filters_list = [
            "todas as linhas",
            "linhas filtradas por data"
        ]

        selected_table = st.selectbox(
            "Selecione a tabela:",
            tables_list,
        )

        if selected_table:
            selected_filter = st.selectbox(
                "Selecione agora o filtro para as linhas:",
                possible_row_filters_list
            )

            st.markdown("*Resultado:*")
            # st.write(f"selected_table: {selected_table}")
            # st.write(f"selected_filter: {selected_filter}")

            query_date = None

            if selected_filter == "linhas filtradas por data":
                query_date = _select_month_and_year_for_filter()

            result_dataframe = pd.DataFrame(
                    APIDataRequester(
                        table=selected_table,
                        row_filter=selected_filter,
                        query_date=query_date
                    )
                )

            st.dataframe(result_dataframe)


def _select_month_and_year_for_filter():
    months_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    years_list = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

    selected_month = st.selectbox(
        "Selecione o mês para o filtro de data:",
        months_list
    )

    selected_year = st.selectbox(
        "Selecione o ano para o filtro de data:",
        years_list
    )

    return str(f'01-{selected_month}-{selected_year}')


if __name__ == '__main__':
    ReadData().execute()
