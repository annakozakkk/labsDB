from t08_flask_mysql.app.my_project.auth.dao import user_has_role
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserHasRoleService(GeneralService):
    """
    Realisation of User service.
    """
    _dao = user_has_role

    def add_relationship(self, user_id, role_id):

        return self._dao.make_many_to_many_connection(user_id, role_id)

