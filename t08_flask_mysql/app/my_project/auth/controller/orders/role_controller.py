from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import role_service


class RoleController(GeneralController):
    """
    Realisation of Role controller.
    """
    _service = role_service
