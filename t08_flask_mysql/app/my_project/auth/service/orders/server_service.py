from t08_flask_mysql.app.my_project.auth.dao import server_dao
from t08_flask_mysql.app.my_project.auth.dao.orders import channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ServerService(GeneralService):
    """
    Realisation of Server service.
    """
    _dao = server_dao

    def insert_server_data(self, server_id:int, name:str, creation_date:str):
        self._dao.insert_server_data(server_id, name, creation_date)


