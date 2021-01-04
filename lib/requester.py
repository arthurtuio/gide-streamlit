import requests
import json

from lib.api_conn_params import HerokuAPIEndpoints, LocalAPIEndpoints


def APIDataGetRequester(table, row_filter, columns=None, query_date=None, tarifas_other_query_params=None):
    gide_api = HerokuAPIEndpoints()

    if row_filter == "todas as linhas":
        endpoint = gide_api.get_all_data_from_table(table)
        response = requests.get(endpoint)

        return response.json()

    elif row_filter == "linhas filtradas por data":
        endpoint = gide_api.get_data_filtered_by_date(table, query_date, tarifas_other_query_params)
        response = requests.get(endpoint)

        return response.json()

    else:
        return None


def APIDataPostRequester(user_inputted_data):
    gide_api = HerokuAPIEndpoints()

    endpoint = gide_api.insert_company_data()
    parsed_data = json.loads(json.dumps(user_inputted_data))

    response = requests.post(
        url=endpoint,
        headers={"Content-Type": "application/json"},
        json=parsed_data
    )

    if response.status_code == 200:
        return "Registro inserido com sucesso no DB!"

    else:
        return "Erro inserindo registro!!"


if __name__ == '__main__':
    # json_result = APIDataGetRequester(table="valor_bandeiras", row_filter="todas as linhas")
    # print(json_result)
    # print(type(json_result))

    data_to_insert = {
        "data_referencia": "01-01-2020",
        "fornecedora": "CELESC",
        "unidade_consumidora": 16666666,
        "nome_cliente": "Teste",
        "modalidade": "Verde",
        "subgrupo": "A4",
        "consumo_ponta": 198,
        "consumo_fora_ponta": 2344,
        "demanda_medida_ponta": 45.72,
        "demanda_medida_fora_ponta": 23.56,
    }

    APIDataPostRequester(data_to_insert)


