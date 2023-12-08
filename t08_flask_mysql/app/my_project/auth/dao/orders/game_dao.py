from datetime import datetime
from typing import List

import sqlalchemy
from flask import jsonify

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Game


class GameDAO(GeneralDAO):
    _domain_type = Game

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Game).filter(Game.name == name).order_by(Game.name).all()

    def find_by_release_date(self, release_date: datetime) -> List[object]:
        return self._session.query(Game).filter(Game.release_date == release_date).order_by(Game.release_date).all()

    def calculate_statistics(self, table_name: str, column_name: str, operation_name: str) -> float:
        try:
            self._session.execute(
                f"CALL calculate_statistics(:p1, :p2, :p3, @result)",
                {"p1": table_name, "p2": column_name, "p3": operation_name}
            )

            while self._session.next_result():
                pass

            result = self._session.execute("SELECT @result").scalar()

            return result

        except Exception as e:

            print(f"Error: {str(e)}")
            self._session.rollback()
