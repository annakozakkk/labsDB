from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship
from t08_flask_mysql.app.my_project.auth.domain.orders.association import user_channel_association
from t08_flask_mysql.app.my_project import db


class Channel(db.Model):
    __tablename__ = 'channel'
    channel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), index=True)
    creation_date = db.Column(db.Date)
    owner = db.Column(db.String(45))
    type = db.Column(db.String(45))
    server_id: int = db.Column(db.Integer, db.ForeignKey('server.server_id') )

    users = db.relationship("User", secondary="users_in_channels", back_populates="channels")

    server = relationship("Server", back_populates="channels")

    def __repr__(self) -> str:
        return (f"Channel({self.channel_id}, {self.name}, {self.creation_date},"
                f" {self.owner}, {self.type}, {self.server_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "channel_id": self.channel_id,
            "name": self.name,
            "creation_date": self.creation_date,
            "owner": self.owner,
            "type": self.type,
            "server_id": self.server_id,
            "users": [{"user_id": user.user_id,
                       "email": user.email,
                       "username": user.username,
                       "about_user": user.about_user,
                       "in_discord": user.in_discord,
                       "game_id": user.game_id,
                       # "messages": [message.put_into_dto() for message in user.messages],
                       # "roles": [{
                       #     "role_id": role.role_id,
                       #     "name": role.name,
                       #     "description": role.description,
                       # } for role in user.roles]

                       } for user in self.users]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Channel:
        obj = Channel(
            channel_id=dto_dict.get("channel_id"),
            name=dto_dict.get("name"),
            creation_date=dto_dict.get("creation_date"),
            owner=dto_dict.get("owner"),
            type=dto_dict.get("type"),
            server_id=dto_dict.get("server_id")
        )
        return obj