
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import  message_service


class MessageController(GeneralController):
    """
    Realisation of Message controller.
    """
    _service = message_service
    def get_statistics(self, Option):
        return message_service.get_procedure(Option)