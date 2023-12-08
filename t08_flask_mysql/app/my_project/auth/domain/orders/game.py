from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db


class Game(db.Model):
    __tablename__ = 'game'
    game_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    release_date = db.Column(db.Date)
    price = db.Column(db.Integer)
    users = relationship("User", back_populates="game")



    def __repr__(self) -> str:
        return f"Game({self.game_id}, {self.name}, {self.release_date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "game_id": self.game_id,
            "name": self.name,
            "release_date": self.release_date,
            "price":self.price,
            "users": [user.put_into_dto() for user in self.users]

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Game:
        obj = Game(
            game_id=dto_dict.get("gameId"),
            name=dto_dict.get("name"),
            release_date=dto_dict.get("release_date"),
            price = dto_dict.get("price")
        )
        return obj
