from datetime import datetime
from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Role


class RoleDAO(GeneralDAO):
    _domain_type = Role

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Role).filter(Role.name == name).order_by(Role.name).all()

    def find_by_description(self, description: str) -> List[object]:
        return self._session.query(Role).filter(Role.description == description).order_by(Role.description).all()

