
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import  server_service


class ServerController(GeneralController):
    """
    Realisation of Server controller.
    """
    _service = server_service

    def insert_server_data(self, server_id_param, name_param, creation_date_param):
        return self._service.insert_server_data(server_id_param, name_param, creation_date_param)

