from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db


class UserHasRole(db.Model):
    __tablename__ = 'users_has_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))
    username = db.Column(db.String(255))
    role_name = db.Column(db.String(255))


    def __repr__(self) -> str:
        return f"UserHasRole({self.id}, {self.user_id}, {self.role_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "role_id": self.role_id,
            "username":self.username ,
            "role_name":self.role_name

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserHasRole:
        obj = UserHasRole(
            id=dto_dict.get("id"),
            user_id=dto_dict.get("user_id"),
            role_id=dto_dict.get("role_id")

        )
        return obj
