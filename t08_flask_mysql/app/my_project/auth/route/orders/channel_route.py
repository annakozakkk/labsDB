from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import channel_controller
from t08_flask_mysql.app.my_project.auth.domain import Channel

channel_bp = Blueprint('channels', __name__, url_prefix='/channels')

@channel_bp.get('')
def get_all_channels() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(channel_controller.find_all()), HTTPStatus.OK)


@channel_bp.post('')
def create_channel() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    channel = Channel.create_from_dto(content)
    channel_controller.create(channel)
    return make_response(jsonify(channel.put_into_dto()), HTTPStatus.CREATED)


@channel_bp.get('/<int:channel_id>')
def get_channel(channel_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(channel_controller.find_by_id(channel_id)), HTTPStatus.OK)


@channel_bp.put('/<int:channel_id>')
def update_channel(channel_id: int) -> Response:
    """
    Updates channel by ID.
    :return: Response object
    """
    content = request.get_json()
    channel = Channel.create_from_dto(content)
    channel_controller.update(channel_id, channel)
    return make_response("Channel updated", HTTPStatus.OK)


@channel_bp.patch('/<int:channel_id>')
def patch_channel(channel_id: int) -> Response:
    """
    Patches channel by ID.
    :return: Response object
    """
    content = request.get_json()
    channel_controller.patch(channel_id, content)
    return make_response("Channel updated", HTTPStatus.OK)


@channel_bp.delete('/<int:channel_id>')
def delete_channel(channel_id: int) -> Response:
    """
    Deletes channel by ID.
    :return: Response object
    """
    channel_controller.delete(channel_id)
    return make_response("Channel deleted", HTTPStatus.OK)
