"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.channel_controller import ChannelController
from .orders.game_controller import GameController
from .orders.message_controller import MessageController
from .orders.server_controller import ServerController
from .orders.user_controller import UserController
from .orders.role_controller import RoleController
from .orders.user_channel_controller import UserInChannelController
from .orders.user_role_controller import UserHasRole

channel_controller = ChannelController()
game_controller = GameController()
message_controller = MessageController()
server_controller = ServerController()
user_controller = UserController()
role_controller = RoleController()
user_channel_controller = UserInChannelController()
user_role_controller = UserHasRole()
