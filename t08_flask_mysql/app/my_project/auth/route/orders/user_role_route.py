from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_role_controller
from t08_flask_mysql.app.my_project.auth.domain import UserHasRole

user_role_bp = Blueprint('users-roles', __name__, url_prefix='/users-roles')

@user_role_bp.get('')
def get_all_users() -> Response:
    """
     Gets all objects from table using Service layer.
     :return: Response object
     """

    return make_response(jsonify(user_role_controller.find_all()), HTTPStatus.OK)


# @user_role_bp.post('')
# def create_user() -> Response:
#     """
#        Gets all objects from table using Service layer.
#        :return: Response object
#     """
#
#     content = request.get_json()
#     user_role = UserHasRole.create_from_dto(content)
#     user_role_controller.create(user_role)
#     return make_response(jsonify(user_role.put_into_dto()), HTTPStatus.CREATED)


@user_role_bp.get('/<int:id>')
def get_user(user_id: int) -> Response:
    """
        Gets user by ID.
        :return: Response object
        """
    return make_response(jsonify(user_role_controller.find_by_id(user_id)), HTTPStatus.OK)


@user_role_bp.put('/<int:id>')
def update_user(id: int) -> Response:
    """
        Updates user by ID.
        :return: Response object
    """

    content = request.get_json()
    user_role = UserHasRole.create_from_dto(content)
    user_role_controller.update(id, user_role)
    return make_response('User updated', HTTPStatus.OK)


@user_role_bp.patch('/<int:id>')
def patch_user(id: int) -> Response:
    """
           Patches user by ID.
           :return: Response object
   """
    content = request.get_json()
    user_role_controller.patch(id, content)
    return make_response('User patched', HTTPStatus.OK)


@user_role_bp.delete('/<int:id>')
def delete_user(id: int) -> Response:
    """
       Deletes user by ID.
       :return: Response object
    """

    user_role_controller.delete(id)
    return make_response("User deleted", HTTPStatus.OK)