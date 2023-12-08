from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.orders.channel import Channel
from t08_flask_mysql.app.my_project.auth.domain.orders.user_channel import UserInChannel


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45))
    username = db.Column(db.String(45))
    about_user = db.Column(db.String(100))
    in_discord = db.Column(db.DateTime)
    game_id: int = db.Column(db.Integer, db.ForeignKey('game.game_id'))
    messages = relationship("Message", back_populates="user")
    channels = db.relationship("Channel", secondary="users_in_channels", back_populates="users")

    game = relationship("Game", back_populates="users")

    roles = db.relationship("Role", secondary="users_has_roles", back_populates="users")

    def __repr__(self) -> str:
        return f"User({self.user_id}, {self.email}, {self.username}, {self.about_user}, {self.in_discord}, {self.game_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "email": self.email,
            "username": self.username,
            "about_user": self.about_user,
            "in_discord": self.in_discord,
            "game_id": self.game_id,
            "channels": [{"channel_id": channel.channel_id,
                          "name": channel.name,
                          "creation_date": channel.creation_date,
                          "owner": channel.owner,
                          "type": channel.type,
                          "server_id": channel.server_id}
                         for channel in self.channels],
            "roles": [{
                "role_id": role.role_id,
                "role_name": role.role_name,
                "description": role.description,
            } for role in self.roles],
            "messages": [message.put_into_dto() for message in self.messages],

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        obj = User(
            user_id=dto_dict.get("user_id"),
            email=dto_dict.get("email"),
            username=dto_dict.get("username"),
            about_user=dto_dict.get("about_user"),
            in_discord=dto_dict.get("in_discord"),
            game_id=dto_dict.get("game_id")
        )
        return obj

