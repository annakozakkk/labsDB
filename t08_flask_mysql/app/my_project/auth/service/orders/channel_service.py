from typing import List

from t08_flask_mysql.app.my_project.auth.dao import channel_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.channel import Channel
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ChannelService(GeneralService):
    """
    Realisation of Channel service.
    """
    _dao = channel_dao

