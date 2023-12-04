from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import server_controller
from t08_flask_mysql.app.my_project.auth.domain import Server

server_bp = Blueprint('servers', __name__, url_prefix='/servers')


@server_bp.get('')
def get_all_servers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(server_controller.find_all()), HTTPStatus.OK)


@server_bp.post('')
def create_server() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    server = Server.create_from_dto(content)
    server_controller.create(server)
    return make_response(jsonify(server.put_into_dto()), HTTPStatus.CREATED)


@server_bp.get('/<int:server_id>')
def get_server(server_id: int) -> Response:
    """
    Gets server by ID.
    :return: Response object
    """
    return make_response(jsonify(server_controller.find_by_id(server_id)), HTTPStatus.OK)


@server_bp.put('/<int:server_id>')
def update_server(server_id: int) -> Response:
    """
    Updates server by ID.
    :return: Response object
    """
    content = request.get_json()
    server = Server.create_from_dto(content)
    server_controller.update(server_id, server)
    return make_response("Server updated", HTTPStatus.OK)

@server_bp.post('/insert-server-data')
def insert_server_data():
    data = request.get_json()
    server_id = data.get('server_id')
    name = data.get('name')
    creation_date = data.get('creation_date')

    server_controller.insert_server_data(server_id, name, creation_date)

    return make_response(jsonify({"message": "Server data inserted successfully"}), HTTPStatus.CREATED)

@server_bp.patch('/<int:server_id>')
def patch_server(server_id: int) -> Response:
    """
    Patches server by ID.
    :return: Response object
    """
    content = request.get_json()
    server_controller.patch(server_id, content)
    return make_response("Server updated", HTTPStatus.OK)


@server_bp.delete('/<int:server_id>')
def delete_server(server_id: int) -> Response:
    """
    Deletes server by ID.
    :return: Response object
    """
    server_controller.delete(server_id)
    return make_response("Server deleted", HTTPStatus.OK)
