from typing import List
from datetime import datetime
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserHasRole


class UserHasRoleDAO(GeneralDAO):
    _domain_type = UserHasRole
