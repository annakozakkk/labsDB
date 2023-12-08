from t08_flask_mysql.app.my_project.auth.dao import user_channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserInChannel(GeneralService):
    """
    Realisation of User service.
    """
    _dao = user_channel_dao
