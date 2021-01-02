import requests
from lib.api_conn_params import HerokuAPIEndpoints, LocalAPIEndpoints

import pandas as pd


def APIDataRequester(table, row_filter, columns=None):
    gide_api = LocalAPIEndpoints()

    if row_filter == "todas as linhas":
        endpoint = gide_api.get_all_data_from_table(table)
        request = requests.get(endpoint)

        return request.json()

    else:
        return None



if __name__ == '__main__':
    json_result = APIDataRequester(table="valor_bandeiras", row_filter="todas as linhas")
    print(json_result)
    print(type(json_result))
