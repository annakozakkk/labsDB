from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db


class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True)
    user_id :int = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    message_text = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime)

    user = relationship("User", back_populates="messages")



    def __repr__(self) -> str:
        return f"Message({self.message_id}, {self.user_id}, {self.message_text}, {self.timestamp})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "message_id": self.message_id,
            "message_text": self.message_text,
            "timestamp": self.timestamp,
            "user_id": self.user_id


        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Message:
        obj = Message(
            message_id = dto_dict.get("message_id"),
            user_id = dto_dict.get("user_id"),
            message_text=dto_dict.get("message_text"),
            timestamp=dto_dict.get("timestamp")

        )
        return obj
