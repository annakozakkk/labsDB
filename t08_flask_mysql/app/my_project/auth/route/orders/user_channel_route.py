from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_channel_controller
from t08_flask_mysql.app.my_project.auth.domain import UserInChannel

user_channel_bp = Blueprint('users-channels', __name__, url_prefix='/users-channels')


@user_channel_bp.get('')
def get_all_users_in_channels() -> Response:
    """
     Gets all objects from table using Service layer.
     :return: Response object
     """

    return make_response(jsonify(user_channel_controller.find_all()), HTTPStatus.OK)


@user_channel_bp.post('')
def create_users_in_channels() -> Response:
    """
       Gets all objects from table using Service layer.
       :return: Response object
    """

    content = request.get_json()
    user_channel = UserInChannel.create_from_dto(content)
    user_channel_controller.create(user_channel)
    return make_response(jsonify(user_channel.put_into_dto()), HTTPStatus.CREATED)


@user_channel_bp.get('/<int:id>')
def get_users_in_channels(id: int) -> Response:
    """
        Gets users_in_channels by ID.
        :return: Response object
        """
    return make_response(jsonify(user_channel_controller.find_by_id(id)), HTTPStatus.OK)


@user_channel_bp.put('/<int:id>')
def update_users_in_channels(id: int) -> Response:
    """
        Updates users_in_channels by ID.
        :return: Response object
    """

    content = request.get_json()
    user_channel = UserInChannel.create_from_dto(content)
    user_channel_controller.update(id, user_channel)
    return make_response('users_in_channels updated', HTTPStatus.OK)


@user_channel_bp.patch('/<int:id>')
def patch_users_in_channels(id: int) -> Response:
    """
           Patches users_in_channels by ID.
           :return: Response object
   """
    content = request.get_json()
    user_channel_controller.patch(id, content)
    return make_response('users_in_channels patched', HTTPStatus.OK)


@user_channel_bp.delete('/<int:id>')
def delete_users_in_channels(id: int) -> Response:
    """
       Deletes users_in_channels by ID.
       :return: Response object
    """

    user_channel_controller.delete(id)
    return make_response("users_in_channels deleted", HTTPStatus.OK)
