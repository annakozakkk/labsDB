from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import message_controller
from t08_flask_mysql.app.my_project.auth.domain import Message

message_bp = Blueprint('messages', __name__, url_prefix='/messages')


@message_bp.get('')
def get_all_message() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(message_controller.find_all()), HTTPStatus.OK)


@message_bp.post('')
def create_message() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    message = Message.create_from_dto(content)
    message_controller.create(message)
    return make_response(jsonify(message.put_into_dto()), HTTPStatus.CREATED)


@message_bp.get('/<int:message_id>')
def get_message(message_id: int) -> Response:
    """
    Gets message by ID.
    :return: Response object
    """
    return make_response(jsonify(message_controller.find_by_id(message_id)), HTTPStatus.OK)

@message_bp.get('use-function/<string:function>')
def get_function(function):
    return make_response(message_controller.get_statistics(function),HTTPStatus.OK)
@message_bp.put('/<int:message_id>')
def update_message(message_id: int) -> Response:
    """
    Updates message by ID.
    :return: Response object
    """
    content = request.get_json()
    message = Message.create_from_dto(content)
    message_controller.update(message_id, message)
    return make_response("Message updated", HTTPStatus.OK)


@message_bp.patch('/<int:message_id>')
def patch_message(message_id: int) -> Response:
    """
    Patches message by ID.
    :return: Response object
    """
    content = request.get_json()
    message_controller.patch(message_id, content)
    return make_response("Message updated", HTTPStatus.OK)


@message_bp.delete('/<int:message_id>')
def delete_message(message_id: int) -> Response:
    """
    Deletes message by ID.
    :return: Response object
    """
    message_controller.delete(message_id)
    return make_response("Message deleted", HTTPStatus.OK)

