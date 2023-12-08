from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db


class Role(db.Model):
    __tablename__ = 'role'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(45))
    description = db.Column(db.String(200))

    users = db.relationship("User", secondary="users_has_roles", back_populates="roles")

    def __repr__(self) -> str:
        return f"Role({self.role_id}, {self.name}, {self.description})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "role_id": self.role_id,
            "role_name": self.role_name,
            "description": self.description,
            "users": [{"user_id": user.user_id,
                       "email": user.email,
                       "username": user.username,
                       "about_user": user.about_user,
                       "in_discord": user.in_discord,
                       "game_id": user.game_id,
                       "messages": [message.put_into_dto() for message in user.messages],
                       "channels": [{"channel_id": channel.channel_id,
                                     "name": channel.name,
                                     "creation_date": channel.creation_date,
                                     "owner": channel.owner,
                                     "type": channel.type,
                                     "server_id": channel.server_id}
                                    for channel in user.channels]

                       } for user in self.users],

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Role:
        obj = Role(
            role_id=dto_dict.get("role_id"),
            role_name=dto_dict.get("role_name"),
            description=dto_dict.get("description"),
        )
        return obj