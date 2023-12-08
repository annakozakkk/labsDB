from datetime import datetime
from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Channel


class ChannelDAO(GeneralDAO):
    _domain_type = Channel

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Channel).filter(Channel.name == name).order_by(Channel.name).all()

    def find_by_creation_date(self, creation_date: datetime) -> List[object]:
        return self._session.query(Channel).filter(Channel.creation_date == creation_date).order_by(
            Channel.creation_date).all()

    def find_by_owner(self, owner: str) -> List[object]:
        return self._session.query(Channel).filter(Channel.owner == owner).order_by(Channel.owner).all()

    def find_by_type(self, type: str) -> List[object]:
        return self._session.query(Channel).filter(Channel.type == type).order_by(Channel.type).all()
