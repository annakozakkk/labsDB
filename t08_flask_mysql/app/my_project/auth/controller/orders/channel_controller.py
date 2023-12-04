from typing import List

from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController
from t08_flask_mysql.app.my_project.auth.service import channel_service


class ChannelController(GeneralController):
    """
    Realisation of Channel controller.
    """
    _service = channel_service


