from cgitb import text
from typing import List, Optional
from datetime import datetime

import sqlalchemy

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Server

class ServerDAO(GeneralDAO):
    _domain_type = Server

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Server).filter(Server.name == name).all()

    def find_by_creation_date(self, creation_date: datetime) -> List[object]:
        return self._session.query(Server).filter(Server.creation_date == creation_date).all()

    def insert_server_data(self, server_id_param, name_param, creation_date_param):
        with self._session() as session:
            result = session.execute(sqlalchemy.text("CALL insert_server_data(:p1, :p2, :p3)"),
                                     {"p1": server_id_param, "p2": name_param, "p3": creation_date_param})
            session.commit()
            return result



