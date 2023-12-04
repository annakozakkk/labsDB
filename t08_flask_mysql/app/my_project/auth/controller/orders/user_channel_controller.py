
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import  user_channel_service


class UserInChannelController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = user_channel_service
