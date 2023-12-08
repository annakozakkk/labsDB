from t08_flask_mysql.app.my_project.auth.dao import game_dao
from t08_flask_mysql.app.my_project.auth.dao.orders import channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class GameService(GeneralService):
    """
    Realisation of Game service.
    """
    _dao = game_dao

    def calculate_statistics(self, table_name, column_name, operation_name):
        result = self._dao.calculate_statistics(table_name, column_name, operation_name)
        return result

