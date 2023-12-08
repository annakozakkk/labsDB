from datetime import datetime
from typing import List

import sqlalchemy
from flask import jsonify

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Message


class MessageDAO(GeneralDAO):
    _domain_type = Message

    def find_by_user_id(self, user_id: int) -> List[object]:
        return self._session.query(Message).filter(Message.user_id == user_id).order_by(Message.user_id).all()

    def find_by_message_text(self, message_text: str) -> List[object]:
        return self._session.query(Message).filter(Message.message_text == message_text).order_by(
            Message.message_text).all()

    def find_by_timestamp(self, timestamp: datetime) -> List[object]:
        return self._session.query(Message).filter(Message.timestamp == timestamp).order_by(Message.timestamp).all()
    def get_procedure(self, option):
        result = self._session.execute(sqlalchemy.text(f"CALL StoredMiwa({option}, @miwa)"))
        if result.returns_rows:
            result = result.scalar()
        else:
            result = None  # Handle the case where there are no rows

        if option == 1:
            return jsonify({'MAX': result})
        elif option == 2:
            return jsonify({'MIN': result})
        elif option == 3:
            return jsonify({'SUM': result})
        else:
            return jsonify({'AVG': result})