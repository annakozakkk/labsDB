from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import game_controller
from t08_flask_mysql.app.my_project.auth.domain import Game

game_bp = Blueprint('games', __name__, url_prefix='/games')



@game_bp.get('')
def get_all_games() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(game_controller.find_all()), HTTPStatus.OK)


@game_bp.post('')
def create_game() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    game = Game.create_from_dto(content)
    game_controller.create(game)
    return make_response(jsonify(game.put_into_dto()), HTTPStatus.CREATED)

@game_bp.post('/calculate_statistic')
def create_statistic():
    data = request.get_json()
    table_name = data.get('table_name')
    column_name = data.get('column_name')
    operation_name = data.get('operation_name')

    result = game_controller.calculate_statistic(table_name, column_name, operation_name)

    return make_response(jsonify({"message": "Calculation successful", "result": result}), HTTPStatus.OK)

@game_bp.get('/<int:game_id>')
def get_game(game_id: int) -> Response:
    """
    Gets game by ID.
    :return: Response object
    """
    return make_response(jsonify(game_controller.find_by_id(game_id)), HTTPStatus.OK)


@game_bp.put('/<int:game_id>')
def update_game(game_id: int) -> Response:
    """
    Updates game by ID.
    :return: Response object
    """
    content = request.get_json()
    game = Game.create_from_dto(content)
    game_controller.update(game_id, game)
    return make_response("Game updated", HTTPStatus.OK)


@game_bp.patch('/<int:game_id>')
def patch_game(game_id: int) -> Response:
    """
    Patches game by ID.
    :return: Response object
    """
    content = request.get_json()
    game_controller.patch(game_id, content)
    return make_response("Game updated", HTTPStatus.OK)


@game_bp.delete('/<int:game_id>')
def delete_game(game_id: int) -> Response:
    """
    Deletes game by ID.
    :return: Response object
    """
    game_controller.delete(game_id)
    return make_response("Game deleted", HTTPStatus.OK)
