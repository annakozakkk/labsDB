"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.channel_route import channel_bp
    from .orders.game_route import game_bp
    from .orders.message_route import message_bp
    from .orders.server_route import server_bp
    from .orders.user_route import user_bp
    from .orders.role_route import role_bp
    from .orders.user_channel_route import  user_channel_bp
    from .orders.user_role_route import  user_role_bp

    app.register_blueprint(channel_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(server_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(user_channel_bp)
    app.register_blueprint(user_role_bp)

