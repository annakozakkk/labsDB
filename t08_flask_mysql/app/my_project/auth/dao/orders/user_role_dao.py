from typing import List
from datetime import datetime

import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserHasRole


class UserHasRoleDAO(GeneralDAO):
    _domain_type = UserHasRole

    def make_many_to_many_connection(self, user_id, role_id):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL make_many_to_many_connection(:user_id, :role_id)"),
                {"user_id": user_id, "role_id": role_id}
            )
            self._session.commit()
            return result
        except Exception as e:
            self._session.rollback()
            raise e