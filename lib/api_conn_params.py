

class HerokuAPIEndpoints:
    HOME = "https://gide-flask-api-write-read.herokuapp.com/"
    GET_ALL = "/api/v1/get/{}/all"

    def get_all_data_from_table(self, table_name):
        if table_name == "valor_tarifas":
            table_endpoint = "tarifas"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        elif table_name == "valor_bandeiras":
            table_endpoint = "bandeiras"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        elif table_name == "valor_impostos":
            table_endpoint = "impostos"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        elif table_name == "empresas_valores_inputados":
            table_endpoint = "empresas_valores_inputados"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        else:
            raise Exception


class LocalAPIEndpoints:
    HOME = "http://0.0.0.0:8080/"
    GET_ALL = "api/v1/get/{}/all"
    GET_BY_DATE = "api/v1/get/{}?data_referencia={}"
    INSERT_COMPANY = "api/v1/insert/empresas_inputadas"

    def get_all_data_from_table(self, table_name):
        if table_name == "valor_tarifas":
            table_endpoint = "tarifas"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        elif table_name == "valor_bandeiras":
            table_endpoint = "bandeiras"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        elif table_name == "valor_impostos":
            table_endpoint = "impostos"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        elif table_name == "empresas_valores_inputados":
            table_endpoint = "empresas_inputadas"
            return self.HOME + self.GET_ALL.format(table_endpoint)

        else:
            raise Exception

    def get_data_filtered_by_date(self, table_name, query_date, tarifas_other_query_params):
        if table_name == "valor_tarifas":
            table_endpoint = "tarifas"

            if tarifas_other_query_params:
                query_string = str(
                    "&fornecedora={}&posto={}&modalidade={}&subgrupo={}".format(
                        tarifas_other_query_params["fornecedora"],
                        tarifas_other_query_params["posto"],
                        tarifas_other_query_params["modalidade"],
                        tarifas_other_query_params["subgrupo"]
                    )
                )

                return self.HOME + self.GET_BY_DATE.format(table_endpoint, query_date) + query_string

            else:
                return self.HOME + self.GET_BY_DATE.format(table_endpoint, query_date)

        elif table_name == "valor_bandeiras":
            table_endpoint = "bandeiras"
            return self.HOME + self.GET_BY_DATE.format(table_endpoint, query_date)

        elif table_name == "valor_impostos":
            table_endpoint = "impostos"
            return self.HOME + self.GET_BY_DATE.format(table_endpoint, query_date)

        elif table_name == "empresas_valores_inputados":
            table_endpoint = "empresas_inputadas"
            return self.HOME + self.GET_BY_DATE.format(table_endpoint, query_date)

        else:
            raise Exception

    def insert_company_data(self):
        return self.HOME + self.INSERT_COMPANY



