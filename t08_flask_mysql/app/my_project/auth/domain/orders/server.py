from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db


class Server(db.Model):
    __tablename__ = 'server'
    server_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    creation_date = db.Column(db.DateTime)
    channels = relationship("Channel", back_populates="server")


    def __repr__(self) -> str:
        return f"Server({self.server_id}, {self.name}, {self.creation_date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "server_id": self.server_id,
            "name": self.name,
            "creation_date": self.creation_date,
            "channels": [channel.put_into_dto() for channel in self.channels]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Server:
        obj = Server(
            server_id = dto_dict.get("server_id"),
            name=dto_dict.get("name"),
            creation_date=dto_dict.get("creation_date")

        )
        return obj
