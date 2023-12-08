from t08_flask_mysql.app.my_project.auth.dao import message_dao
from t08_flask_mysql.app.my_project.auth.dao.orders import channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class MessageService(GeneralService):
    """
    Realisation of Message service.
    """
    _dao = message_dao
    def get_procedure(self, String_function):
        if String_function == "MAX" or String_function == "max":
            return message_dao.get_procedure(1)
        elif String_function == "MIN" or String_function == "min":
            return message_dao.get_procedure(2)
        elif String_function == "SUM" or String_function == "sum":
            return message_dao.get_procedure(3)
        else:
            return message_dao.get_procedure(4)