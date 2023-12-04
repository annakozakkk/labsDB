from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import role_controller
from t08_flask_mysql.app.my_project.auth.domain import Role

role_bp = Blueprint('roles', __name__, url_prefix='/roles')


@role_bp.get('')
def get_all_roles() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(role_controller.find_all()), HTTPStatus.OK)


@role_bp.post('')
def create_role() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    role = Role.create_from_dto(content)
    role_controller.create(role)
    return make_response(jsonify(role.put_into_dto()), HTTPStatus.CREATED)


@role_bp.get('/<int:role_id>')
def get_role(role_id: int) -> Response:
    """
    Gets role by ID.
    :return: Response object
    """
    return make_response(jsonify(role_controller.find_by_id(role_id)), HTTPStatus.OK)


@role_bp.put('/<int:role_id>')
def update_role(role_id: int) -> Response:
    """
    Updates role by ID.
    :return: Response object
    """
    content = request.get_json()
    role = Role.create_from_dto(content)
    role_controller.update(role_id, role)
    return make_response("Role updated", HTTPStatus.OK)


@role_bp.patch('/<int:role_id>')
def patch_role(role_id: int) -> Response:
    """
    Patches role by ID.
    :return: Response object
    """
    content = request.get_json()
    role_controller.patch(role_id, content)
    return make_response("Role updated", HTTPStatus.OK)


@role_bp.delete('/<int:role_id>')
def delete_role(role_id: int) -> Response:
    """
    Deletes role by ID.
    :return: Response object
    """
    role_controller.delete(role_id)
    return make_response("Role deleted", HTTPStatus.OK)
