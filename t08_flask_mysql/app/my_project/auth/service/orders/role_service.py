from t08_flask_mysql.app.my_project.auth.dao import role_dao
from t08_flask_mysql.app.my_project.auth.dao.orders import channel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class RoleService(GeneralService):
    """
    Realisation of Role service.
    """
    _dao = role_dao
