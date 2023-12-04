from flask import jsonify

from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import game_service


class GameController(GeneralController):
    """
    Realisation of Game controller.
    """
    _service = game_service

    def calculate_statistic(self, table_name, column_name, operation_name):
        result = self._service.calculate_statistics(table_name, column_name, operation_name)
        return result




