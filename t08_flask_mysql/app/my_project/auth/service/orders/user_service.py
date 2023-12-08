from t08_flask_mysql.app.my_project.auth.dao import user_dao
from t08_flask_mysql.app.my_project.auth.dao.orders import channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserService(GeneralService):
    """
    Realisation of User service.
    """
    _dao = user_dao

    def insert_rows(self):
        self._dao.insert_rows()

