
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import  user_role_service


class UserHasRole(GeneralController):
    """
    Realisation of User controller.
    """
    _service = user_role_service

    def add_relationship(self, user_id, role_id):
        return self._service.add_relationship(user_id, role_id)
