from datetime import datetime
from typing import List

import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import User
from t08_flask_mysql.app.my_project.auth.domain.orders.role import Role


class UserDAO(GeneralDAO):
    _domain_type = User

    def find_by_email(self, email: str) -> List[object]:
        return self._session.query(User).filter(User.email == email).order_by(User.email).all()

    def find_by_username(self, username: str) -> List[object]:
        return self._session.query(User).filter(User.username == username).order_by(User.username).all()

    def find_by_in_discord(self, in_discord: datetime) -> List[object]:
        return self._session.query(User).filter(User.in_discord == in_discord).order_by(User.in_discord).all()

    def find_by_game_id(self, game_id: int) -> List[object]:
        return self._session.query(User).filter(User.game_id == game_id).order_by(User.game_id).all()

    def insert_rows(self):
        with self._session() as session:

            session.execute(sqlalchemy.text("CALL insert_rows()"))

            session.commit()


