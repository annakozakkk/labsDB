
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import  user_service


class UserController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = user_service

    def insert_rows(self):
        return self._service.insert_rows()

