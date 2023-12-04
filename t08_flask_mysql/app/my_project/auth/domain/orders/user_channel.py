from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db


class UserInChannel(db.Model):
    __tablename__ = 'users_in_channels'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.channel_id'))


    def __repr__(self) -> str:
        return f"UsersInChannel({self.id}, {self.user_id}, {self.channel_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "channel_id": self.channel_id,


        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserInChannel:
        obj = UserInChannel(
            id=dto_dict.get("id"),
            user_id=dto_dict.get("user_id"),
            channel_id=dto_dict.get("channel_id")
        )
        return obj
